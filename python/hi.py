#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
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

msg.send()
