# urlDiffCheck

## An exploration of various ways to alert user of change in source of specific webpage, through console and/or email

At first pass targeted for windows machines, however can be used on Unix with some tweaking  
This README may have some errors - please contact me if such is the case

### Method 1 - Run a python script from command line
Open checkURLNoTask.py, fill out the variables in the headers:
- `secondsToSleep` - number of seconds between runs.  3600 = 1 hour
- `numberOfTimes` - number of times to run - anything less that 0 will run forever!
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
**NOTE2:** My script, due to some package dependencies, requires Python 3.  If you do not have the latest python version (as is the case with the default EC2 Amazon server out of box) or Python 3 is not the default Python version, a simple solution is to change the `python` keyword to `python34`, as in `python34 checkURLNoTask.py`


### Method 2 - Windows Methods
Here are some of the methods I tried to give me results:  
* You may put my `bashScript.sh`, or any bash script for that matter, into the Task Scheduler to schedule the script to run upon machine startup, machine unlocking, etc.  The drawback here is that you will only get alerts when your machine is awake. Refer to [this](http://www.howtogeek.com/123393/how-to-automatically-run-programs-and-set-reminders-with-the-windows-task-scheduler/) guide for more details: 
* You my put a **shortcut copy** of `bashScript.sh` into your Windows Startup folder, where it will be run on startup.  Same problem as above.  Find where your Startup folder is by pressing Start -> Type run.exe -> type `shell:startup`
* Upload your python script to a www.pythonanywhere.com account, where you can run small python programs in the cloud for free.  I thought this would be the best method because with a free account I'd be able to run my simple script but unfortunately the site I want to check is not whitelisted for a free account.  
  
Other solutions - interested to hear.  Without paying, I was not able to figure out a way thus far to make this happen. Perhaps deploying Django on a Heroku service with the script somehow deployed would be acceptable, but I have yet to try this.

### Method 3 - On Linux/Unix, set up a cron task
First, I got myself the free version of the Amazon EC2 account, which gives 750 hours/month free for the first year.  This is enough for my purposes.  
After setting up my free linux virtual machine (refer to the Amazon guide for instructions) I ssh'ed in and cloned my project. I set my variables with email/pass/website, and was able to run my script. Now I need to schedule a cron task to run my script on a timer - that way I can just set it and forget it!