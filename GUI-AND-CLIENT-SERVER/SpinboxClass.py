#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from FramePerso import * 


class SpinboxClass:
	"""docstring for SpinboxClass"""
	def __init__(self, name,window,minValue,maxValue,position,margex,margey):
		self.name=name
		self.maxValue=maxValue
		self.minValue=minValue
		self.position=position
		if type(window) is FramePerso :
			self.label=Label(window.getFrame(),text=name)
			self.spin= Spinbox(window.getFrame(), from_=minValue, to=maxValue)
		else:
			self.label=Label(window,text=name)
			self.spin= Spinbox(window, from_=minValue, to=maxValue,command=self.checkValue)
		self.label.pack(side=position)
		self.spin.pack(side=position,padx=margex,pady=margey)


	def getValue(self):
		return int(self.spin.get())

	def hide(self):
		self.label.pack_forget()
		self.spin.pack_forget()

	def show(self):
		self.label.pack(side=self.position)
		self.spin.pack(side=self.position)
		

	def changeConfig(self,min,max):
		self.spin.config(from_=min,to=max)

	#def checkValue():
	#	if self.spin.get()>self.maxValue:
	#		self.spin.icursor(self.maxValue-self.minValue-1)
		