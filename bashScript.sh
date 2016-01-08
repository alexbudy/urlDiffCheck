#!/bin/bash
# very simple bash script 

# arg here is seconds between runs (default is coded as 3600 in py script)
python checkURLNoTask.py -s 1800

#doesnt get here since py script in inf loop
sleep 10