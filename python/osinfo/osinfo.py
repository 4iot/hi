#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform

def get_os_info_linux():
    rinfo = platform.linux_distribution()
    if (rinfo[1] == ''):
        info = None
    else:
        info = {}
        info['os'] = 'Linux'
        info['release'] = rinfo[0]
        info['version'] = rinfo[1]
        info['machine'] = rinfo[2]
    
    return info

def get_os_info_windows():
    return None
    
def get_os_info_mac():
    rinfo = platform.mac_ver()
    if (rinfo == None):
        info = None
    else:
        info = {}
        info['os'] = 'MacOS'
        info['version'] = rinfo[0]
        info['arch'] = rinfo[2]
    
    return info

def get_os_info():
    info = None
    
    info = get_os_info_linux()
    
    if not info:
        info = get_os_info_windows()
        
    if not info:
        info = get_os_info_mac()
    
    return info
    
    