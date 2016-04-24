#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform
import subprocess


def get_network_interfaces():
    ifaces = {}
    
    res = subprocess.check_output("ifconfig", "-a")
    print res
    
    return ifaces

get_network_interfaces()
