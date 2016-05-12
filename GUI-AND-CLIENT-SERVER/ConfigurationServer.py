#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from client_server import Client

##
#Class which save server configuration information
# basically this class save : ip, port,client id , number of packet to send , type of protocol (ie : spi , i2c ,uart) , time betwen packets 

class ConfigurationServer:
    def __init__(self):
        self.ip = 'localhost'
        self.port = -1
        self.client = None
        self.protocol = -1
        self.time = -1
        self.packet_number = 0

    ##
    #@return ip to connect
    def get_ip(self):
        return self.ip

    ##
    #@return port to connect
    def get_port(self):
        return self.port

    ##
    #set ip value 
    #@param ip : ip value
    def set_ip(self, ip):
        self.ip = ip
    ##
    #set port value
    #@param port:  port  value
    def set_port(self, port):
        self.port = port

    ##
    #set protocol value(ie i2c or uart or spi)
    #@param  bus_protocol : protocol value
    def set_protocole(self, bus_protocol):
        if bus_protocol == "UART":
            self.protocol = 0
        elif bus_protocol == "SPI":
            self.protocol = 1
        elif bus_protocol == "I2C":
            self.protocol = 2
    ##
    #@return protocol choice
    def get_protocol(self):
        return self.protocol
    ##
    #set number of packet to send 
    def set_packet_number(self, number):
        self.packet_number = number

    ##
    #@return number of packet to send
    def get_packet_number(self):
        return self.packet_number

    ##
    #set time between packets
    #@param time : time value between packets
    def set_packet_time(self, time):
        self.time = time

    ##
    #connect function
    #@return True if the connection success, False otherwise 
    def connect(self):
        print(self.ip)
        print(self.port)
        self.client = Client.Client(self.ip, self.port)
        if self.client.connect():
            print("Connected")
            return True
        return False  # there was an error while connecting

    ##
    # disconnect Function
    def disconnect(self):
        self.client.close_socket()
        print("Connection closed")
    ##
    # send a mess to the raspberry with the basic configuration to run 
    def send_mes(self):
        if self.client is not None:
            self.client.send_message(self.packet_number, self.protocol, self.time)
            # print("data send")

