#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   round.py
@Time    :   2024/02/19 16:06:01
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   None
'''

import math as m 

in_fl = float(input("Input a floating number: "))

ans = int(m.floor(in_fl))

print(f'The round number down of {in_fl} is equal to: {ans}')