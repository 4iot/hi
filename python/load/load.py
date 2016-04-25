#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import subprocess
import sys

sys.path.append('../osinfo')
from osinfo import OsInfo

class Load:
    
    __osi = None
    
    def __init__(self):
        self.__osi = OsInfo()

    def getCpuLoad(self):
        res = subprocess.check_output(['sh', '-c', 'ps -e -o %cpu | awk \'{s+=$1} END {print s}\''])
        return float(res)

    def getStorageStatus(self):
        res = subprocess.check_output(['sh', '-c', 'df -k | grep "/dev/" | grep -v tmp']).splitlines()
        drives = {}
        index = 0;
        count = len(res)
        
        while index < count:
            current = res[index].split()
            drive = {}
            if (self.__osi.isMacOS() == True):
                drive['dev'] = current[0]
                drive['used'] = int(current[2])
                drive['avail'] = int(current[3])
                drive['mount'] = current[8]
            elif (self.__osi.isLinux() == True):
                drive['dev'] = current[0]
                drive['used'] = current[2]
                drive['avail'] = current[3]
                drive['mount'] = current[5]
            else:
                print 'Error: unknown OS'
            if (len(drive) > 0):
                drives[drive['mount']] = drive
                del drive['mount']
            index += 1
            
        return drives

#l = Load()
#print l.getCpuLoad()
#print l.getStorageStatus()

