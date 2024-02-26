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

fruits = ["banana","orange","lemon","pear"]

idx = rd.randint(0,len(fruits)-1)

print(f'This is a randomly generated fruit: {fruits[idx]}')
