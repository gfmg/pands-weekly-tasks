#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   sub.py
@Time    :   2024/02/19 15:41:14
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   None
'''
import random as rd

print("Generate a random number from the range given by:")

num_one = int(input("Number one: "))
num_two = int(input("Number two: "))

rd_number = rd.randint(num_one,num_two)
print(f'Here is a random number from {num_one} to {num_two}: {rd_number}')