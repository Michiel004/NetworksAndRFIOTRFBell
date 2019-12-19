#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
import os
import updateNode
import smtplib
import sendMail
from time import sleep
from gnuradio import gr

class comparator_py_f(gr.sync_block):
    """
    docstring for block comparator_py_f
    """
    def __init__(self, value):
	self.value = value
	self.counter = 0
	self.isReady = 0
	self.isOn = 0
	gr.sync_block.__init__(self,
		name="comparator_py_f",
		in_sig=[numpy.float32],
		out_sig=None)


    def work(self, input_items, output_items):
        in0 = input_items[0]

	try:
	    if self.counter >= 100:
	        self.isReady = 1
	        self.counter = 0
	    else:
	        self.counter = self.counter + 1

	    for items in input_items:
		for item in items:
		    if item > self.value:
				if self.isReady == 1:
						updateNode.setNode2()
						sendMail.send()
						print("on")
						self.isReady = 0
						self.isOn = 1
		    else: 
				if self.isOn == 1:
					updateNode.resetNode2()	
					print("off")
					self.isOn = 0
        
	except:
	    print("error") 
        return len(input_items[0])

