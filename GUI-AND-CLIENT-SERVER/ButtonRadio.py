#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from FramePerso import * 

class ButtonRadio:
	"""docstring for ButtonRadio"""
	def __init__(self, name,window,position,associate_field,option,optionValue):
		self.name=name
		self.value=StringVar()
		self.optionValue=optionValue
		self.associate_field=associate_field
		self.list_option=["button"]*len(option)
		for ind,elt  in enumerate(list(option)):
			self.list_option[ind]+=str(ind)#change option name
			if type(window) is FramePerso :
				self.list_option[ind]=Radiobutton(window.getFrame(), text=elt, variable=self.value, value=ind,command=self.changeConfigAssociateField)
			else:
				self.list_option[ind]=Radiobutton(window, text=elt, variable=self.value, value=ind,command=self.changeConfigAssociateField)
			self.list_option[ind].pack(side=position)
		self.associate_field.show()

	def getValue(self):
		return self.value.get()

	def changeConfigAssociateField(self):
		min,max=self.optionValue[int(self.value.get())]
		self.associate_field.changeConfig(min,max)

	def getChoice(self):
		return self.value.get()
		
		
		
