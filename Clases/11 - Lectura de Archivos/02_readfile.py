#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:59:06 2021

@author: danielaudd
"""

file = open('2020-05-01-CasosConfirmados.csv', 'r') #Abre el archivo
data = file.read()
print (data)
file.close() # Cierra el archivo