#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform

def get_os_info_linux(cinfo = None):
    rinfo = platform.linux_distribution()
    if (rinfo[1] == ''):
        info = None
    else:
        info = {}
        info['os'] = 'Linux'
        info['dist'] = rinfo[0]
        info['version'] = rinfo[1]
        if (cinfo != None):
            info['arch'] = cinfo['arch']
        else:
            info['arch'] = platform.processor()
        info['kernel'] = platform.uname()[2]
    
    return info

def get_os_info_windows(cinfo = None):
    return None
    
def get_os_info_mac(cinfo = None):
    rinfo = platform.mac_ver()
    if (rinfo == None):
        info = None
    else:
        info = {}
        info['os'] = 'MacOS'
        info['dist'] = 'X'
        info['version'] = rinfo[0]
        info['arch'] = rinfo[2]
        info['kernel'] = platform.uname()[2]
    
    return info

def get_os_info(cinfo = None):
    info = None
    
    info = get_os_info_linux(cinfo)
    
    if not info:
        info = get_os_info_windows(cinfo)
        
    if not info:
        info = get_os_info_mac(cinfo)
    
    return info
    
    