#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from EntryText import EntryText
from ConfigurationServer import ConfigurationServer
from scrollField import scrollField
from FramePerso import FramePerso
from tkinter import *
from Buton import *
from SpinboxClass import * 
from ButtonRadio import * 

#main window 
win = Tk()
win.title('Cubsat interface')
win.geometry('{}x{}'.format(500, 450))
win.resizable(width=FALSE, height=FALSE)  # not allowed to change window size

#list which contains all widgets, allowed to show some widgets when we are connected,and not before
list_widgets=[]

entry_ip = EntryText("IP MAITRE", win, "localhost", TOP, 0, 5)  # 0 : the field is an IP adress
entry_port = EntryText("PORT", win, "10003", TOP, 0, 5)  # 1 : the field is a port
config_server = ConfigurationServer()
connect_button = ConnectButon("Connect", win, entry_ip, entry_port, config_server,list_widgets)

# ================= THESE WIDGETS WILL BE SHOW AFTER CONNECTION =============

#-------PROTOCOL CONFIGURATION-----#
frame_protocol_config = FramePerso("Protocol Configuration",win,RIGHT,60,60)
list_widgets.append(frame_protocol_config)
entry_packet_number = EntryText("Nombre de paquet", frame_protocol_config, "Number of packets", TOP, 5, 15) 
entry_packet_time = EntryText("temps entre les packets", frame_protocol_config, "Time between packets", TOP, 5, 15)
scroll_choice_protocol = scrollField("Protocol Choice",frame_protocol_config,TOP,["SPI", "UART", "I2C"])  # choose a protocol
send_button = SendButton("Send", frame_protocol_config, entry_packet_number, entry_packet_time, config_server, scroll_choice_protocol,BOTTOM)

#TODO : ADD LABEL % LOST PACK 

#-----------SALEAE CONFIGURATION---------#
frame_saleae_config = FramePerso("Saleae Configuration",win,LEFT,60,60)
list_widgets.append(frame_saleae_config)

entry_analog_channel = SpinboxClass("Number Of analog channels", frame_saleae_config,0,8 ,TOP,2,2)
entry_digital_channel = SpinboxClass("Number Of digital channels", frame_saleae_config,0,8 ,TOP,2,2)
entry_analog_sample_rate= SpinboxClass("Analog Sample Rate", frame_saleae_config, 4e6,100e9 ,TOP,2,2) 
entry_digital_sample_rate= SpinboxClass("Digital Sample Rate", frame_saleae_config, 4e6, 100e9,TOP,2,2) 

scroll_choice_trigger =  scrollField("Trigger Choice",frame_saleae_config,TOP,["Rising Edge", "Falling Edge"]) #choose trigger, ajouter plus tard les deux options manquantes

entry_capture_time_and_sample_number= SpinboxClass("", frame_saleae_config, 0, 100,BOTTOM,1,1)
field_length_capture_to_edit= ButtonRadio("field_capture",frame_saleae_config,LEFT,entry_capture_time_and_sample_number,["Capture Time(seconds) ","Sample Number"],[(0,100),(4e6,100e9)])




#send 
#send_saleae_conf= SendSaleaeButton("Send",frame_saleae_config,BOTTOM,entry_analog_channel ,entry_digital_channel,entry_analog_sample_rate,entry_digital_sample_rate,scroll_choice_trigger,field_length_capture_to_edit)

win.mainloop() #run

