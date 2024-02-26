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

in_one=int(input(f"Enter number one: "))
in_two=int(input(f"Enter number two: "))

ans = int(in_one // in_two)
rem = in_one%in_two

print(f'{in_one} divided by {in_two} is equal to: {ans} and remainer {rem}')