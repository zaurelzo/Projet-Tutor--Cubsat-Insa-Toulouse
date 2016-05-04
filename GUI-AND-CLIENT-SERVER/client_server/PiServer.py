#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import socket
import sys

UART = 0
SPI = 1
I2C = 2


class Server:
    def __init__(self, name, port, message_queue):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (name, port)
        self.message_queue = message_queue

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
                    (packet, protocol) = pickle.loads(data)
                    print('received "%d %d"' % (packet, protocol))
                    if data:
                        self.message_queue.put((packet, protocol))  # add message to buffer queue
                    else:
                        break
            except socket.error:
                print("Connection broke", file=sys.stderr)
            except EOFError:
                pass  # TODO this is not the most beautiful way to do it. Normaly the stream should be closed before pickle
            finally:
                print("client disconnected")
                connection.close()