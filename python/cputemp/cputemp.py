#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import platform
import subprocess

def get_cpu_temp_windows():
    import wmi
    import pythoncom
    def temperature_reader():
        pythoncom.CoInitialize()
        w = wmi.WMI(namespace='root\\wmi')
        temperature = w.MSAcpi_ThermalZoneTemperature()[0].CurrentTemperature
        temperature = int(temperature / 10.0 - 273.15)
        return temperature
    return temperature_reader

def get_cpu_temp_mac():
    return subprocess.check_output(["./bin/macosx_i386/osx-cpu-temp"])

def get_cpu_temp_linux():
    return None

def get_cpu_temp():
    temp = None
    
    # Platform detection
    os_name = platform.system()
    if os_name == 'Windows':
        temp = get_cpu_temp_windows()
    elif os_name == 'Darwin':
        temp = get_cpu_temp_mac()
    elif os_name == 'Linux':
        temp = get_cpu_temp_linux()
        
    return temp
