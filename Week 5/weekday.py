#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   weekday.py
@Time    :   2024/02/26 13:56:43
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   Week 5 weekly Task. Return weekday or weekend based on current date
'''
import datetime as dt # Import the datetime package and cal it "dt"

inp=dt.datetime.now() # Return current date. From package "dt" the function datetime.now()
#print(inp) is the current date (Year, Month, Day,Hour, Minut, Seconds)
res=inp.weekday() # We know extract as result (res), the week number from inp. From 0 (Monday) to 6 (Sunday) 
                  # Anything below 5 is weekday...5 or 6 is weekend. 

if res < 5: #If our week day number is below 5 
    print("Yes, unfortunately today is a weekday.")
else: # Otherwise
    print("It is the weekend, yay!")