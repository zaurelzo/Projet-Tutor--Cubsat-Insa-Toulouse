#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import socket
import sys

UART = 0
SPI = 1
I2C = 2

##
# This is the server which waits for connection with the client and accepts the transmitted commands.
class Server:

    ##
    # @param name: Server name or ip
    # @param port: Port on which the server should be opened
    # @param message_queue: Synchronized message queue to communicate which the SerialSender class
    def __init__(self, name, port, message_queue):

        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (name, port)
        self.message_queue = message_queue

    ##
    # Starts up the server and waits for connection of a client.
    # Incoming message are saved in the message queue. The actual sending of the packets is done by another thread
    # from the SerialSender class.
    def listen(self):
        print('starting up on %s port %s' % self.server_address)
        self.sock.bind(self.server_address)
        self.sock.listen(1)

        while True:
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                print('client connected:', client_address)
                while True:
                    data = connection.recv(4096)
                    (packet, protocol, time) = pickle.loads(data)
                    print('received "%d %d %f"' % (packet, protocol, time))
                    if data:
                        self.message_queue.put((packet, protocol, time))  # add message to buffer queue
                    else:
                        break
            except socket.error:
                print("Connection broke", file=sys.stderr)
            except EOFError:
                pass #to avoid false EOF errors from pickle
            finally:
                print("client disconnected")
                connection.close()