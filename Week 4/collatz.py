#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   collatz.py
@Time    :   2024/02/26 12:28:13
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   Week 4 weekly Task. Working with while loops
'''

inp=int(input("Please enter a positive integer: ")) #inp as an integer input

#Check input is positive
while inp < 0: #Rather than using an if statement, we can check thay while the number is negative, we keep asking for a positive integer
        inp=int(input("The number you entered is negative. Please enter a positive integer: "))

# When the input is not negative:        
print(inp) #Print the input
while inp !=1: #until inp not equals 1
        if inp%2==0: # if even divide by 2:
            inp=int(inp/2) #Update sequence
            print(inp) #Print updated number
        else: # otherwise multiply by 3 and add 1
            inp=int((inp*3)+1) #Update sequence
            print(inp) #Print updated number
