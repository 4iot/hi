#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from sense_hat import SenseHat
from HiMessage import HiMessage

msg = HiMessage()

if (len(sys.argv) > 0):
    index = 1
    message = ""
    while (index < len(sys.argv)):
        message += sys.argv[index] + ' '
        index += 1
    message = message.rstrip()

if (message != None) and (message != ""):
    msg.info(message)


sense = SenseHat()
humidity = sense.get_humidity()
temp = sense.get_temperature() - 32.4 + 21.1
pressure = sense.get_pressure()

msg.add("humidity", humidity)
msg.add("temp", temp)
msg.add("pressure", pressure)

msg.send()

sense.set_rotation(180)
red = (255, 0, 0)
orange = (255, 165, 0)

sense.show_message("Hum:" + str("%.1f" % humidity) + "%")

tempF = temp*1.800+32.00
sense.show_message("Temp:" + str("%.1f" % temp) + "C/" + str("%.1f" % tempF) + "F", text_colour=red)

sense.show_message("Pre:" + str("%.0f" % pressure) + "mbar", text_colour=orange)


