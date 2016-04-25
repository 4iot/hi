#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess

def get_cpu_load():
    res = subprocess.check_output(['sh', '-c', 'ps -e -o %cpu | awk \'{s+=$1} END {print s}\''])
    return float(res)

print get_cpu_load()