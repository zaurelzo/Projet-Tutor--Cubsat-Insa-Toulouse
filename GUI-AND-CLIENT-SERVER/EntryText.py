#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from FramePerso import * 
import sys


class EntryText:
    """class for input user """

    def __init__(self, name, window, text,position,*marge):

        #self.type = type  # 0 :IP, 1:Port
        self.window = window
        self.name = name
        result = StringVar()
        self.position=position
        result.set(text)
        if type(window) is FramePerso: #because window can be an FramePerso object, 
            self.champ = Entry(window.getFrame(), textvariable=result, bg='bisque')
        else:
            self.champ = Entry(window, textvariable=result, bg='bisque')
        self.champ.focus_set()
        self.x , self.y = marge
        self.champ.pack(side=position, padx=self.x, pady=self.y)
        self.value = result.get()  #bidouille

    def get_value(self):
        return self.champ.get()

    #def get_type(sealf):
        #return self.type

    def get_int_value(self):
        try:
            re = int(self.champ.get())
            return re
        except Exception:
            print("Please enter only numbers in the packet number field", file=sys.stderr)
            return -1


    def hide(self):
        self.champ.pack_forget()

    def show(self):
        self.champ.pack(side=self.position, padx=self.x, pady=self.y)

    def notEditable(self):
        self.champ.config(state=DISABLED)