#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pyserial import *

class SerialSender:

    def __init__(self, message_queue):
        self.message_queue = message_queue
        try:
            self.port = Serial("/dev/ttyAMA0", baudrate=115200, timeout=1.0)
            self.debug = False
        except OSError:
            print("/dev/ttyAMA0 was not found. Looks like you are testing on your computer, sending of serials was disabled", file=sys.stderr)
            self.debug= True

    def run(self, args, args2):
        while(True):
            number, protocol = self.message_queue.get(True)
            for i in range(0, number):
                if not self.debug:
                    self.port.write("ping") #todo send with the right protocol
                else:
                    print("pseudo sended a serial packet", file=sys.stderr)
