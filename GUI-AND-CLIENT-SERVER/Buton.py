#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *
from FramePerso import * 
from saleae import *  #use saleae analyser



class ConnectButon:
    """class for a Buton"""

    def __init__(self, name, window, EntryFieldIP, EntryFieldPort, config,widget_list):
        self.ip_field = EntryFieldIP
        self.port_field = EntryFieldPort
        self.widget_list=widget_list
        self.config = config
        self.name = name
        self.is_connected = False
        self.client_server = None
        self.b1 = Button(window)
        self.b1.config(text=name, command=self.connect)
        self.b1.pack()  # draw button

    # TODO :faire une regexp pour verfifier Si l'IP  ou le port est valide
    def connect(self):
        self.config.set_ip(self.ip_field.get_value())
        self.config.set_port(int(self.port_field.get_value()))
        if self.config.connect():  # if connected 
            self.b1.config(text="Disconnect", command=self.disconnect)
            self.is_connected = True
            for elt in self.widget_list:#show frames
                elt.show()


    def disconnect(self):
        self.b1.config(text="Connect", command=self.connect)
        self.config.disconnect()
        self.is_connected = False
        for elt in self.widget_list:
            elt.hide()

    def isConnected(self):
        return self.is_connected


class SendButton:
    """class for a Button"""

    def __init__(self, name, window, entry_field_number_of_packet, config, scroll_choice,position):
        self.nb_packet = entry_field_number_of_packet
        self.config = config
        self.position=position
        self.scrollChoice = scroll_choice
        if type(window) is FramePerso:
            self.b1 = Button(window.getFrame())
        else:
            self.b1 = Button(window.getFrame())

        self.b1.config(text=name, command=self.send)
        self.b1.pack(side=position, padx=5, pady=5)  # bidouillage pour afficher à la bonne position

    def send(self):
        self.config.set_protocole(self.scrollChoice.getChoice())
        self.config.set_packet_number(self.nb_packet.get_int_value())
        self.config.send_mes()
        print("data send")

    def show(self):
        self.b1.pack(side=self.position, padx=5, pady=15)  # bidouillage pour afficher à la bonne position



class SendSaleaeButton:
    """docstring for SendSaleaeButton"""
    def __init__(self,name,window,position,Nb_AnaLog_chan,Nb_dig_chan,Analog_sample_rate,Dig_sample_rate,triggerChoice,cap_time_or_sample_number):
        self.name=name
        self.Nb_AnaLog_chan=Nb_AnaLog_chan
        self.Nb_dig_chan=Nb_dig_chan
        self.Analog_sample_rate=Analog_sample_rate
        self.Dig_sample_rate=Dig_sample_rate
        self.triggerChoice=triggerChoice
        self.cap_time_or_sample_number=cap_time_or_sample_number
        self.position=position
        if type(window) is FramePerso:
            self.b1 = Button(window.getFrame())
        else:
            self.b1 = Button(window.getFrame())
        self.b1.config(text=name, command=self.send)
        self.b1.pack(side=position, padx=5, pady=25) 

        
    def send(self):
        saleae.demo()
        