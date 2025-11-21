#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 10:20:01 2021

@author: danielaudd
"""


#imprime las potencias de 2 desde 0 hasta n
#codigo más complejo
n = int(input('ingresa un numero: '))
a = True
v = 1
i = 0
while a == True:
    print('la variable v es:', v)
    i = i + 1
    v = 2*v
    if i>n:
        a = False