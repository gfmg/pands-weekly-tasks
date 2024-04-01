#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   bank.py
@Time    :   2024/02/03 22:42:47
@Author  :   Guillermo Martin
@Version :   1.0
@Personal email : gfmg1992@hotmail.com
@Student email: G00438885@atu.ie
@License :   (C)Copyright 2023, Guillermo Martin
@Desc    :   Weekly Task 02. Bank programme. Takes two inputs as cents and return the total amount in euros
'''

i1 = int(input("Enter amount 1 (in cent): ")) #input1 (i1): integer
i2 = int(input("Enter amount 2 (in cent): ")) #input2 (i2): integer 

res = (i1 + i2)/100 #res (result) defines the sum of input 1 and input 2 and divides it by 100 (to transform in euros)

print(f"The total amount= \N{euro sign}{res}") #Print the result (res). We have included the euro sign before res by using \N{euro sign}