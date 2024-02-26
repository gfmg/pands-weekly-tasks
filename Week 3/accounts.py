#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   accounts.py
@Time    :   2024/02/26 09:36:40
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   Weekly task. Topic 3 
'''

anum = str(input("Please enter your account number: ")) #Account number

numlen=len(anum)

ans=anum[-4:] #Last four digits
x="X"*(numlen-4) # X repeated the length of the bank account minus 4

print(f"{x}{ans}")
