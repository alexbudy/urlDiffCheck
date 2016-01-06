# the simplest solution - simply run this script at startup 
# - output will go to console and alert if there is a diff
# For first run will compare with specified html file
# 	or create new one if nonexistant

secondsToSleep = 3600 # default value = 1 hour. Override with flag

def checkUrl():
	print "running"

if __name__ == "__main__":
	while True:
		checkUrl()
		time.sleep(secondsToSleep) #