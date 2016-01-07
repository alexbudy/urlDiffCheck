# urlDiffCheck

## An exploration of various ways to alert user of change in source of specific webpage, through console and/or email

At first pass targeted for windows machines, however can be used on Unix with some tweaking  
This README may have some errors - please contact me if such is the case

### Method 1 - Run a python script from command line
Open checkURLNoTask.py, fill out the variables in the headers:
- `secondsToSleep` - number of seconds between runs.  3600 = 1 hour
- `urlToCheck` - which URL you want to check
- `fileToWrite` - which file will store the last run source, any name would work  
**Email variables**
- `sendEmailFlag` - if true, script will attempt to send email report if there is a diff
- `emailDest` - email(s) to send to (if multiple, provide in list form:[a,b,c])
- `emailType` - email formatting: 'html' or 'plain' only  
	**Important Email Variables**
- `emailSrc` - I used GMail service to send emails.  If you want to use the service, you will need a gmail account.  Read below
- `emailSrcPass` - password to corresponding email. Read below note for more info (This is not your raw email password!)

To run the script, open a terminal (if on Windows you will need to install Python - google for instructions) and run this:

`python checkURLNoTask.py`

or run `python checkURLNoTask.py -h` to view command line options


Keep this running for as long as you want, just know that when your computer shuts down/goes to sleep the script will stop as well.


**NOTE:**  To be able to send python email through the gmail SMTP server you will need to generate an 'application-specific' password. [Here](https://support.google.com/accounts/answer/185833) is Google's page regarding this.  Simply generate a password here, then paste it into `checkURLNoTask.py` script in the password field to allow email sending.  
**CAREFUL** - make sure to remove this password when committing - otherwise this password may become available to the public!


### Method 2 - Use Windows Task Scheduler

### Method 3 - On Linux/Unix, set up a cron task