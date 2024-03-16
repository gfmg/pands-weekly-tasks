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
@Desc    :   Weekly Task 02. Bank programme
'''

# Pramme to add two numbers together and print as euros 

i1 = int(input("Enter amount 1 (in cent): ")) #input1: interger
i2 = int(input("Enter amount 2 (in cent): ")) #input2: integer 

res = (i1 + i2)/100 

print(f"The total amount= \N{euro sign}{res}")

#print "Please pay %s"%(u"\N{euro sign}")