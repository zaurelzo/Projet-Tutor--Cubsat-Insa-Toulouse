#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PiServer import Server
from SerialSender import SerialSender
#from concurrent.futures.thread import start_new_thread
#from threading import Thread
import threading
import _thread
from queue import Queue

message_queue = Queue()

serial_sender = SerialSender(message_queue)
_thread.start_new_thread(serial_sender.run, (0, 0))

server = Server('0.0.0.0', 10005, message_queue)

server.listen()