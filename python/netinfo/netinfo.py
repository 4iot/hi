#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform
import subprocess


def get_network_interfaces():
    if (platform.system() == 'Darwin'):
        return get_network_interfaces_mac()
    else:
        return get_network_interfaces_linux()

def get_network_interfaces_linux():
    ifaces = {}
    iface = {}
    
    res = subprocess.check_output(['ifconfig', '-a']).splitlines()
    length = len(res)
    index = 0
    context = ''
    while (index < length):
        currentLine = res[index]
        if (currentLine[0].isspace() != True):
            # New context
            context = res[index].split()[0]
            if (len(iface) > 0):
                if (('mac' in iface) and (('ipv4' in iface) or ('ipv6' in iface))):
                    ifaces[iface['name']] = iface
                    del iface['name']
            iface = {}
            iface['name'] = context
        else:
            # analyze the line
            values = currentLine.split()
            if (values[0] == 'ether'):
                iface['mac'] = values[1]
            elif (values[0] == 'inet'):
                iface['ipv4'] = values[1]
            elif (values[0] == 'inet6'):
                iface['ipv6'] = values[1]
        index += 1
    return ifaces

def get_network_interfaces_mac():
    ifaces = {}
    iface = {}
    
    res = subprocess.check_output(['ifconfig', '-a']).splitlines()
    length = len(res)
    index = 0
    context = ''
    while (index < length):
        currentLine = res[index]
        if (currentLine[0].isspace() != True):
            # New context
            context = res[index].split(':')[0]
            if (len(iface) > 0):
                if (('mac' in iface) and (('ipv4' in iface) or ('ipv6' in iface))):
                    ifaces[iface['name']] = iface
                    del iface['name']
            iface = {}
            iface['name'] = context
        else:
            # analyze the line
            values = currentLine.split()
            if (values[0] == 'ether'):
                iface['mac'] = values[1]
            elif (values[0] == 'inet'):
                iface['ipv4'] = values[1]
            elif (values[0] == 'inet6'):
                iface['ipv6'] = values[1]
        index += 1
    return ifaces
