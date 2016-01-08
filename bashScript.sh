# very simple bash script

# arg here is seconds between runs (default is coded as 3600 in py script)
# ever half hour, 5 times
# set up cron eery 3 hours
python34 /home/ec2-user/urlDiffCheck/checkURLNoTask.py -s 1800 -r 5