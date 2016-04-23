#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import json
import urllib2
import platform
import cpuinfo
import datetime
import time
import osinfo

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
        self.__data['timestamp'] = now.isoformat()
        info = cpuinfo.get_cpu_info()
        self.__data['cpu'] = format(info['brand'])
        self.__data['os'] = osinfo.get_os_info()
        
    def send(self):
        if (self.__debug == True):
            url = 'http://localhost:8080/io.oplo.receiver/hi'
        else:
            url = 'http://api.4iot.io/io.oplo.receiver/hi'
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        try:
            response = urllib2.urlopen(req, json.dumps(self.__data))
            the_page = response.read()
            print the_page
        except:
            print "HTTP Post error"

    def add(self, key, value):
        self.__data[key] = value
        
    def info (self, msg):
        if ( msg != None ): 
            self.__data['msg'] = msg


        