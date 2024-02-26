#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   round.py
@Time    :   2024/02/19 16:06:01
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   Extra excercise of the math fun! Transform dollar and cent input to an absolute cent value
'''

import decimal as dc

in_fl = dc.Decimal(input("Please enter an amount of dollars: "))

ans = round(abs(in_fl)*100,0)

print(f'The amount {in_fl} dollars in cents is: {ans}')