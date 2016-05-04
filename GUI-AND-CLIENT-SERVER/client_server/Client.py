#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import pickle


class Client:

    def __init__(self, name, port):
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        self.server_address = (name, port)

    def connect(self):
        print('connecting to %s port %s' % self.server_address)
        try:
            self.sock.connect(self.server_address)
            return True
        except Exception:
            print("Connection refused", file=sys.stderr)
            return False

    def send_message(self, packet_number, protocol):
        message = (packet_number, protocol)
        print('sending "%d, %d"' % (packet_number, protocol))
        self.sock.sendall(pickle.dumps(message))

    def send_test_message(self):
        try:
            # Send data
            message = 'This is the message.  It will be repeated.'
            print ('sending "%s"' % message)
            self.sock.sendall(message)

            # Look for the response
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = self.sock.recv(16)
                amount_received += len(data)
                print('received "%s"' % data)
        except:
            print('Error in send test', file=sys.stderr)

    def close_socket(self):
        print('closing socket')
        self.sock.close()
