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
    temp = subprocess.check_output(["./bin/macosx_i386/osx-cpu-temp"]).strip()
    return temp

def check_hardware():
    import os
    if os.path.exists("/sys/devices/LNXSYSTM:00/LNXTHERM:00/LNXTHERM:01/thermal_zone/temp") == True:
        return  4
    elif os.path.exists("/sys/bus/acpi/devices/LNXTHERM:00/thermal_zone/temp") == True:
        return  5              
    elif os.path.exists("/proc/acpi/thermal_zone/THM0/temperature") == True:
        return  1
    elif os.path.exists("/proc/acpi/thermal_zone/THRM/temperature") == True:
        return  2
    elif os.path.exists("/proc/acpi/thermal_zone/THR1/temperature") == True:
        return  3       
    elif os.path.exists("/opt/vc/bin/vcgencmd") == True:
        return  6      
    else:
        return 0

def get_cpu_temp_from_hardware(hardware):
    if hardware == 1 :
        temp = open("/proc/acpi/thermal_zone/THM0/temperature").read().strip().lstrip('temperature :').rstrip(' C')
    elif hardware == 2 :
        temp = open("/proc/acpi/thermal_zone/THRM/temperature").read().strip().lstrip('temperature :').rstrip(' C')
    elif hardware == 3 :
        temp = open("/proc/acpi/thermal_zone/THR1/temperature").read().strip().lstrip('temperature :').rstrip(' C')
    elif hardware == 4 :
        temp = open("/sys/devices/LNXSYSTM:00/LNXTHERM:00/LNXTHERM:01/thermal_zone/temp").read().strip().rstrip('000')
    elif hardware == 5 :
        temp = open("/sys/bus/acpi/devices/LNXTHERM:00/thermal_zone/temp").read().strip().rstrip('000')
        temp = str(float(temp)/10.0)
    elif hardware == 6: # RPI
        temp = subprocess.check_output(["/opt/vc/bin/vcgencmd","measure_temp"]).strip().lstrip('temp=').rstrip('\'C')
    else:
        return None
    return temp

def get_cpu_temp_linux():
    hardware = check_hardware();
    if (hardware == 0):
        print 'Hardware not identified'
        return None
    return get_cpu_temp_from_hw(hardware)


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
