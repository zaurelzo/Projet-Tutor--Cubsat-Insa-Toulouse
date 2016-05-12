#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from FramePerso import * 

##
#ButtonRadio conctructor
#@param name  :window's name
#@param window : main window
#@param postion :button position 
#@param associate_field:  field wich is linked with the button radio
#@param option : list different option to choose (ex ["caputre_time,capture_sample"])
#@param optionValue : list of tuple which contains the min and max value for each option(ex for the previous example of option [(1,50) ,(100,200)]) 

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


	##
	#return selected option value 
	def getValue(self):
		return self.value.get()
	##
	# allowed to change the min and max value of spinbox box associate to each option which belong to parameter option of the constructor
	def changeConfigAssociateField(self):
		min,max=self.optionValue[int(self.value.get())]
		self.associate_field.changeConfig(min,max)

	##
	#@return current button radio value 
	def getChoice(self):
		return self.value.get()
	##
	#@return the current value of the associate field (ie : the spinbox value )
	def getValueOFAssociateField(self):
		return self.associate_field.getValue()

		
		
		
