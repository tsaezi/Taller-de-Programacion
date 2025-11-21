#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 09:17:25 2021

@author: danielaudd
"""
from datetime import datetime

date_str1 = '6/6/18' #fecha estilo 1
date_str2 = '06-06-2018' #fecha estilo 2

print(type(date_str1))

date_dt1 = datetime.strptime(date_str1, '%d/%m/%y')

print(date_dt1)

print(type(date_dt1))

date_dt1.day



