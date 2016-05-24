#!/bin/bash

# Simple message to send sensor data

export PATH=$PATH:/sbin

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
python $dir/hisensor.py $*
