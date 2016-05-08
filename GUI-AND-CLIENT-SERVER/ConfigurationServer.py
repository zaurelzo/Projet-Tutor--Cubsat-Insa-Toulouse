#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from client_server import Client

class ConfigurationServer:
    def __init__(self):
        self.ip = 'localhost'
        self.port = -1
        self.client = None
        self.protocol = -1
        self.time = -1
        self.packet_number = 0

    def get_ip(self):
        return self.ip

    def get_port(self):
        return self.port

    def set_ip(self, ip):
        self.ip = ip

    def set_port(self, port):
        self.port = port

    def set_protocole(self, bus_protocol):
        if bus_protocol == "UART":
            self.protocol = 0
        elif bus_protocol == "SPI":
            self.protocol = 1
        elif bus_protocol == "I2C":
            self.protocol = 2

    def get_protocol(self):
        return self.protocol

    def set_packet_number(self, number):
        self.packet_number = number

    def get_packet_number(self):
        return self.packet_number

    def set_packet_time(self, time):
        self.time = time

    # demander à Marc de faire verifier le retour de connecter pour etre sur que ça a marché
    def connect(self):
        print(self.ip)
        print(self.port)
        self.client = Client.Client(self.ip, self.port)
        if self.client.connect():
            print("Connected")
            return True
        return False  # there was an error while connecting

    def disconnect(self):
        self.client.close_socket()
        print("Connection closed")

    def send_mes(self):
        if self.client is not None:
            self.client.send_message(self.packet_number, self.protocol, self.time)
            # print("data send")

