#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   accounts.py
@Time    :   2024/02/26 09:36:40
@Author  :   Guillermo Martin
@Version :   1.0
@Contact :   gfmg1992@hotmail.com
@License :   (C)Copyright 2024-, Guillermo Martin
@Desc    :   Weekly task. Topic 3. Takes an account number and returns the blank account blanked except the last 4 digits
'''

anum = str(input("Please enter your account number: ")) #Account number (anum), defined as a string

alen=len(anum) #Account number length (anum). Aka: number of digits in the account
ans=anum[-4:] #Answer (ans). Select the last four digits of the acount number (anum)
x="X"*(alen-4) # X repeated the length of the bank account minus 4

print(f"{x}{ans}") #Print the repeated X, together with the last four digit answer (ans)
