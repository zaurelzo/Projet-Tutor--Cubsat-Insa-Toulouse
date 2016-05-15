#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


##
# Class for creating new frames inside of the GUI window
class FramePerso:

    ##
    # FramePerso constructor : to create a new frame inside the main window
    # @param name window's name
    # @param window main window
    # @param position frame position
    # @param height frame height
    # @param width frame width
    def __init__(self, name, window, position, height, width):
        self.name = name
        self.position = position
        self.frame = LabelFrame(window, text=name, borderwidth=2, relief=GROOVE, width=width, height=height)
        self.frame.pack_forget()  #by defaut ,hide

    # self.label1=Label(self.frame,text=name)
    # self.label1.pack_forget()

    ##
    # show the current frame
    def show(self):
        self.frame.pack(side=self.position)

    # self.label1.pack(side=TOP,padx=5,pady=5)

    ##
    # hide the current frame
    def hide(self):
        self.frame.pack_forget()

    # self.label1.pack_forget()

    ##
    # return the current frame
    def getFrame(self):
        return self.frame
