#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import urllib2
import platform
import cpuinfo
import cputemp
import datetime
import time
from osinfo import OsInfo
import netinfo
from load import Load
import sys
from urllib2 import HTTPError

class HiMessage:
    "Sends and manages a Hi message to the server"
    
    __debug = False
    
    def __init__(self, msg=None, seq=None):
        self.reset()
        if ( msg != None ) : 
            self.__data['msg'] = msg
        if ( seq != None ) : 
            self.__data['seq'] = seq

    def reset(self):
        self.__data = {}
        now = datetime.datetime.now()
        self.__data['seq'] = int(round(time.time() * 1000))
        self.__data['timestamp-client'] = now.isoformat()
        cinfo = cpuinfo.get_cpu_info()
        self.__data['cpu'] = format(cinfo['brand'])
        osinfo = OsInfo()
        oinfo = osinfo.getOsInfo(cinfo)
        self.__data['os'] = oinfo['os']
        self.__data['os-dist'] = oinfo['dist']
        self.__data['os-version'] = oinfo['version']
        self.__data['os-arch'] = oinfo['arch']
        self.__data['os-kernel'] = oinfo['kernel']
        self.__data['cpu-temp'] = cputemp.get_cpu_temp()
        l = Load()
        self.__data['cpu-load'] = l.getCpuLoad()
        self.__data['storage'] = l.getStorageStatus()
        self.__data['network'] = netinfo.get_network_interfaces()
        
    def send(self):
        if (self.__debug == True):
            url = 'http://localhost:8080/ROOT/hi'
        else:
            url = 'http://api.4iot.io/hi'
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        try:
            response = urllib2.urlopen(req, json.dumps(self.__data))
        except HTTPError as e:
            print ("HTTP Post error: #%d (%s), while connecting to %s." % (e.code, e.reason, url))
            return

        the_page = response.read()
        print the_page

    def add(self, key, value):
        self.__data[key] = value
        
    def info (self, msg):
        if ( msg != None ): 
            self.__data['msg'] = msg


        