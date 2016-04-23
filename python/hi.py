#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from HiMessage import HiMessage

msg = HiMessage()

message = sys.argv[1]
if message != None:
    msg.info(message)

msg.send()
