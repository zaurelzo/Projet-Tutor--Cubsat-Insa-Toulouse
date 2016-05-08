#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import pickle


class Client:
    """This client transmits commands from the GUI to the server.

    """

    def __init__(self, name, port):
        """
        @param name The name can either be a hostname or an ip adress
        @param port The port on wich the server is running.
        """
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        self.server_address = (name, port)

    def connect(self):
        """Establishes the connection to the server.

        :return: True if connected, False if an error occured
        """
        print('connecting to %s port %s' % self.server_address)
        try:
            self.sock.connect(self.server_address)
            return True
        except Exception:
            print("Connection refused", file=sys.stderr)
            return False

    def send_message(self, packet_number, protocol, time):
        """Sends the passed values to the connected server.

        :param packet_number: Number of serials packets that should be sended
        :param protocol: Type of serial protocol. Defined in the PiServer class.
        :param time: time between sending of the serial packets.
        :return: No return
        """
        message = (packet_number, protocol, time)
        print('sending "%d, %d, %f"' % (packet_number, protocol, time))
        self.sock.sendall(pickle.dumps(message))

    def close_socket(self):
        """Closes the connection to the server.

        :return: No return
        """
        print('closing socket')
        self.sock.close()