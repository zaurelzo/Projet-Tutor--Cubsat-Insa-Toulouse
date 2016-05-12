#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from tkinter import *
from FramePerso import *
from saleae import *  # use saleae analyser
import traceback


class ConnectButon:
    """class for a Buton"""

    def __init__(self, name, window, EntryFieldIP, EntryFieldPort, config, widget_list):
        self.ip_field = EntryFieldIP
        self.port_field = EntryFieldPort
        self.widget_list = widget_list
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
            for elt in self.widget_list:  # show frames
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

    def __init__(self, name, window, entry_field_number_of_packet, entry_field_time_of_packet, config, scroll_choice,
                 position):
        self.nb_packet = entry_field_number_of_packet
        self.time_packet = entry_field_time_of_packet
        self.config = config
        self.position = position
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
        self.config.set_packet_time(self.time_packet.get_int_value())
        self.config.send_mes()
        print("data send")

    def show(self):
        self.b1.pack(side=self.position, padx=5, pady=15)  # bidouillage pour afficher à la bonne position


class SendSaleaeButton:
    """docstring for SendSaleaeButton"""

    def __init__(self, name, window, position, Nb_AnaLog_chan, Nb_dig_chan, Analog_sample_rate, Dig_sample_rate,
                 triggerChoice, cap_time_or_sample_number):
        self.name = name
        self.Nb_AnaLog_chan = Nb_AnaLog_chan
        self.Nb_dig_chan = Nb_dig_chan
        self.Analog_sample_rate = Analog_sample_rate
        self.Dig_sample_rate = Dig_sample_rate
        self.triggerChoice = triggerChoice
        self.cap_time_or_sample_number = cap_time_or_sample_number
        self.position = position
        if type(window) is FramePerso:
            self.b1 = Button(window.getFrame())
        else:
            self.b1 = Button(window)
        self.b1.config(text=name, command=self.send)
        self.b1.pack(side=position, padx=1, pady=1)


    def send(self):
        try:
            s = saleae.Saleae()  # by defaut, send to localhost and port 10429
            print("Saleae connected.")
        except ConnectionRefusedError:
            print("Saleae seems to be not running, please start it and try again", file=sys.stderr)
            return

        try:
            s.set_performance(saleae.PerformanceOption.Full)
            print("Set performance to full.")
        except s.CommandNAKedError:
            print("Could not set performance.")  # better to draw a error window

        devices = s.get_connected_devices()
        print("Connected devices:")

        for device in devices:
            print("\t{}".format(device))

        digital = [w for w in range(self.Nb_dig_chan.getValue())]
        analog = [w for w in range(self.Nb_AnaLog_chan.getValue())]
        # print("digital channels :")
        #print(digital)
        #print("analog channels")
        #print(analog)

        try:
            s.set_active_channels(digital, analog)
        except Exception:
            print("Problem with Saleae API, check if it is running and the analyzer is connected", file=sys.stderr)
            return

        digital, analog = s.get_active_channels()
        print("Reading back active channels:")
        print("\tdigital={}\n\tanalog={}".format(digital, analog))

        #rate = s.set_sample_rate_by_minimum(self.Dig_sample_rate.getValue(), self.Analog_sample_rate.getValue())
        #print("\tRate set to", rate)

        trig = saleae.Trigger.NoTrigger
        if self.triggerChoice.getChoice() == "Rising Edge":
            trig = saleae.Trigger.High
            print("Trigger ready set to high")
        else:
            trig = saleae.Trigger.Low
            print("Trigger ready set to low")


        #set trigger for active digital channels #FTODO IXER CETTE SALOPERIE
        try:
            if len(digital) > 0:
                channels = [trig for w in digital]
                print(channels)
                s.set_triggers_for_all_channels(channels)
        except s.ImpossibleSettings:
            print("Could not set Trigger")
        except s.CommandNAKedError as e:
            #e = traceback.format_exc()
            #print(e)
            print("FIX THIS BUG ")

        print("TIGGER set to : {} ".format(trig))

        print("choice {}".format(self.cap_time_or_sample_number.getChoice()))

        if int(str(self.cap_time_or_sample_number.getChoice())) == 0:
            print("capture with Time : {} seconds".format(self.cap_time_or_sample_number.getValueOFAssociateField()))
            s.set_capture_seconds(self.cap_time_or_sample_number.getValueOFAssociateField())
        elif int(str(self.cap_time_or_sample_number.getChoice())) == 1:
            print("Capture with sample number : {}".format(self.cap_time_or_sample_number.getValueOFAssociateField()))
            s.set_num_samples(self.cap_time_or_sample_number.getValueOFAssociateField())
        else:
            print("NO CHOICE ")

        s.capture_start_and_wait_until_finished()  #start capture and wait

        #need to export datas and treat them
        #s.export_data("/home/marc/testLogic/test")
        s.save_to_file("/home/marc/testLogic/test2")