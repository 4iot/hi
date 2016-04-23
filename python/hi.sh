#!/bin/bash

dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
python $dir/hi.py $1
