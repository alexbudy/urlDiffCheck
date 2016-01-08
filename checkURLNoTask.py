# the simplest solution - simply run this script at startup 
# - output will go to console and alert if there is a diff
# For first run will compare with specified html file
# 	or create new one if nonexistant
import time
import urllib.request as ur
from sys import argv
import sys, getopt
import argparse
import os.path
from datetime import datetime
import difflib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

##   If you are going to recommit this file with your own information, look for no-comit hooks
   # These hooks will filter sensitive information on my machine, but will not do so on your machine	 

# logging setup
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='tmp.log',
                    filemode='w')

### default params, can be passed as flags to change
secondsToSleep = 3600 # 3600s = 1hr 
urlToCheck = "www.Google.com" #no-commit
fileToWrite = "sourceOfLastRun.html" # file with last source of site
verbose = True # if True, print 
log = True # if True, write to log

# email parameters
sendEmailFlag = True
emailDest = ["www.Google.com"]  #no-commit, make a list if multiple recipients
emailType = 'html' # can also be html.  Other values will break!
#############

### Values to be set by modifying this file only, not thru command line
emailSrc = emailDest[0] # change here if dest is different than from
emailSrcPass = "www.Google.com"  #no-commit this password generated from https://support.google.com/accounts/answer/185833
									# refer to README.md for more details
#############


def checkUrl():
	with ur.urlopen(urlToCheck) as openedUrl:
		fetchedHtml = str(openedUrl.read().decode('utf-8'))

	if (os.path.isfile(fileToWrite)):
		currentFileHtml = open(fileToWrite).read()
		if (currentFileHtml == fetchedHtml):
			writeLine("same at " + createTimeStamp())
		else:
			writeFileBack(fetchedHtml)
			writeLine("diff at " + createTimeStamp())
			diff = getDiffString(currentFileHtml, fetchedHtml)
			emailDiff(diff)

	else:
		writeFileBack(fetchedHtml, True)
		checkUrl()

# feel free to modify this function as needed to 'prettify' your email bodies	
def emailDiff(diff):
	if (sendEmailFlag):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(emailSrc, emailSrcPass)
		 
		msg = createMIMEMsg(diff)

		server.sendmail(emailSrc, emailDest, msg.as_string())
		server.quit()

def createMIMEMsg(txt):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'Latest diff of webpage "www.Google.com"' #no-commit
	msg['To'] = emailDest[0]

	txt += "\n\n\n\n\n\nURL of webpage: " + urlToCheck
	html =  MIMEText(txt, emailType)

	msg.attach(html)
	return msg
	

def writeFileBack(src, created = False,):
	with open(fileToWrite, 'w') as f:
		f.write(src)
	if (created):
		action = 'created'
	else:
		action = 'overwritten'

	writeLine("		File " + action + " at " + createTimeStamp())

def getDiffString(orig, new):
	d = difflib.HtmlDiff()
	diff = list(difflib.context_diff(orig.splitlines(), new.splitlines()))
	diff = [line[1:] for line in diff if line[0] == '!'] # the '!' corresponds with difflib for diff presentation
	return '\n'.join(list(diff))

# prints a simple time stamp for readibility
def createTimeStamp():
	now = datetime.now()
	return now.strftime("%b %d, %Y at %I:%M.%S %p")

def writeLine(s):
	if verbose:
		print(s)
	if log:
		logging.info(s)

if __name__ == "__main__":
	opts, args = getopt.getopt(sys.argv[1:],"hs:",["seconds="])

	for opt, arg in opts:
		if opt == '-h':
			print('python checkURLNoTask.py -s <seconds>')
			sys.exit()
		elif opt in ("-s", "--seconds"):
			secondsToSleep = int(arg)

	line = "checking url: " + urlToCheck + " every " + str(secondsToSleep) + " seconds with email sending: " + str(sendEmailFlag)
	writeLine(line)
	
	while True:
		checkUrl()
		time.sleep(secondsToSleep) 
