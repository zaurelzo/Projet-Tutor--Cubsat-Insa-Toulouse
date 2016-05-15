#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from FramePerso import *


##
# Spinbox class for the GUI
class SpinboxClass:

    ##
    # spinbox contructor
    # @param name window's name
    # @param window main window
    # @param minValue minimum value for the spinbox text field
    # @param maxValue maximum value for the spinbox text field
    # @param position spinbox position
    # @param margex marge for x axis
    # @param margey marge for y axis
    def __init__(self, name, window, minValue, maxValue, position, margex, margey):
        self.name = name
        self.maxValue = maxValue
        self.minValue = minValue
        self.position = position
        if type(window) is FramePerso:
            self.label = Label(window.getFrame(), text=name)
            self.spin = Spinbox(window.getFrame(), from_=minValue, to=maxValue)
        else:
            self.label = Label(window, text=name)
            self.spin = Spinbox(window, from_=minValue, to=maxValue, command=self.checkValue)
        self.label.pack(side=position)
        self.spin.pack(side=position, padx=margex, pady=margey)

    ##
    # return current spinbox value
    def getValue(self):
        return int(self.spin.get())

    ##
    # hide the spinbox
    def hide(self):
        self.label.pack_forget()
        self.spin.pack_forget()

    ##
    # show the spinbox
    def show(self):
        self.label.pack(side=self.position)
        self.spin.pack(side=self.position)

    ##
    # change spinbox min and max value
    def changeConfig(self, min, max):
        self.spin.config(from_=min, to=max)

        # def checkValue():
        # if self.spin.get()>self.maxValue:
        # self.spin.icursor(self.maxValue-self.minValue-1)