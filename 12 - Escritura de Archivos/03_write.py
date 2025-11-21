#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:41:37 2020

@author: danielaudd
"""



data = ["Línea 1", "Línea 2", "Línea 3", "Línea 4", "Línea 5"]
file = open('archivo3.txt', 'w')

for line in data:
    file.write(line)
    file.write('\n')
file.close()