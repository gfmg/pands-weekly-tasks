#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   weekday.py
@Time    :   2024/02/26 13:56:43
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   Return weekday or weekend based on current date
'''
import datetime as dt

inp=dt.datetime.now() # Return current date
res=inp.weekday() #Anything below 5 is weekday...5 or 6 is weekend. 

if res < 5:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")