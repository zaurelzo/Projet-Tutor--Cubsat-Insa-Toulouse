#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append("/usr/local/lib/python3.4/dist-packages")
sys.path.append("/usr/local/lib/python3/dist-packages")
from serial import *


class SerialSender:
    """This class runs a thread which sends the serial packets.

    """

    def __init__(self, message_queue):
        """Tries to use the ttyAMA0 connection. If it is not availible the class will run in a debug mode which is
        not actually sending packages.

        :param message_queue: The synchronized message queue to communicate with the Server class
        """
        self.message_queue = message_queue
        try:
            self.port = Serial("/dev/ttyAMA0", baudrate=115200, timeout=1.0)
            self.debug = False
        except OSError:
            print(
                "/dev/ttyAMA0 was not found. Looks like you are testing on your computer, sending of serials was disabled",
                file=sys.stderr)
            self.debug = True

    def run(self, args, args2):
        """The thread function which sends the packets.

        :param args: Not use only needed because of python standards
        :param args2: Not use only needed because of python standards
        """
        while True:
            number, protocol, time_between = self.message_queue.get(True)

            last_packet_time = 0
            sended_packets = 0
            while sended_packets < number:
                if time.time() > last_packet_time + time_between:
                    if not self.debug:
                        self.port.write("ping")  # todo send the right packet type
                    else:
                        print("pseudo sended a serial packet", file=sys.stderr)
                    last_packet_time = time.time()
                    sended_packets += 1