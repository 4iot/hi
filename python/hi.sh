#!/bin/bash

# Simple message sender, you can add as many arguments as you want, they will be added as a message

# This script can be inserted in your crontab:
# $ sudo crontab -e
#
# Add:
# */2 * * * * /home/pi/Documents/hi/python/hi.sh
#
# This will send a message every 2 minutes

export PATH=$PATH:/sbin

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
python $dir/hi.py $*
