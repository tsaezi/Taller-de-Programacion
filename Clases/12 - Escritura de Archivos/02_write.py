#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:41:37 2020

@author: danielaudd
"""
data = ["Daniela", "Paula", "Eduardo", "Ricardo", "Hugo"]

file = open("archivo3.txt", "w")
for line in data:
    print(line)
    file.write(line)
  
file.close()
