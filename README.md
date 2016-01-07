# urlDiffCheck

## An exploration of various ways to alert user of change in source of specific webpage, through console and/or email

### At first pass targeted for windows machines, however can be used on Unix with some tweaking

NOTE:  To be able to send python email through the gmail SMTP server you will need to generate an 'application-specific' password. [Here](https://support.google.com/accounts/answer/185833) is Google's page regarding this.  Simply generate a password here, then paste it into `checkURLNoTask.py` script in the password field to allow email sending.  
**CAREFUL** - make sure to remove this password when committing - otherwise this password may become available to the public!