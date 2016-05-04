#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *

class FramePerso:
	"""docstring for Frame"""
	def __init__(self , name ,window,position,height,width):
		self.name=name
		self.position=position
		self.frame=LabelFrame(window,text=name,borderwidth=2,relief=GROOVE,width=width,height=height)
		self.frame.pack_forget()#by defaut ,hide
		#self.label1=Label(self.frame,text=name)
		#self.label1.pack_forget()

	def show(self):
		self.frame.pack(side=self.position)
		#self.label1.pack(side=TOP,padx=5,pady=5)

	def hide(self):
		self.frame.pack_forget()
		#self.label1.pack_forget()

	def getFrame(self):
		return self.frame

		