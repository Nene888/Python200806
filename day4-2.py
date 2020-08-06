# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:05:39 2020

@author: USER
"""

file=open("weee.jpg",'rb')
img=file.read()
file.close() 

file=open("thge.jpg",'wb')
file.write(img)
file.close() 
