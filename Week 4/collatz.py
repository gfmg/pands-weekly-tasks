#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   collatz.py
@Time    :   2024/02/26 12:28:13
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   Week 4 weekly Task
'''

inp=int(input("Please enter a positive integer: ")) #inp as input

#Check input is positive
if inp < 0:
        inp=int(input("The number you entered is negative. Please enter a positive integer: "))
       
print(inp)
while inp !=1: #until inp not equals 1
        if inp%2==0: # if even divide by 2:
            print(int(inp/2))
            inp=int(inp/2) #Update sequence
        else: # otherwise multiply by 3 and add 1
            print(int((inp*3)+1))
            inp=int((inp*3)+1) #Update sequence
