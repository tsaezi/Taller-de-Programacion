#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:57:40 2021

@author: danielaudd
"""


from sys import argv
n = int(argv[1])
i = 0
v = 1

while i <= n:
    print(v)
    i = i + 1
    v = 2*v