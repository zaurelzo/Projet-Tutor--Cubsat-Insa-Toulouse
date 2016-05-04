#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from  EntryText import EntryText
from FramePerso import *


class scrollField:
    def __init__(self, name,window,position,listOption):
        # choix du protocole
        self.OPTIONS = listOption
        if type(window) is FramePerso:
        	self.variable = StringVar(window.getFrame())
        else:
        	self.variable = StringVar(window)
        self.variable.set(self.OPTIONS[0])  # default value
        if type(window) is FramePerso:
        	self.w = OptionMenu(*(window.getFrame(), self.variable) + tuple(self.OPTIONS))
        	self.label=Label(window.getFrame(),text=name)
        else: 
        	self.w = OptionMenu(*(window, self.variable) + tuple(self.OPTIONS))
        	self.label=Label(window,text=name)
        self.label.pack(side=position)	
        self.w.pack(side=position,padx=5,pady=1)

    def getChoice(self):
        return self.variable.get()


