#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   es.py
@Time    :   2024/03/06 22:03:15
@Author  :   Guillermo Martin
@Version :   1.0
@Personal email : gfmg1992@hotmail.com
@Student email: G00438885@atu.ie
@License :   (C)Copyright 2023, Guillermo Martin
@Desc    :   Reading a file and output the number of e's it contains
'''

import os
import sys

# Piece of code from real python: https://realpython.com/command-line-interfaces-python-argparse/
# Argument 1 is the name of the file es.py
# Argument 2 is the name of the .txt file we want to open
# So, in terminal "python es.py week7text.py" is a total of 2 arguments....
if (args_count := len(sys.argv)) > 2: # args_count is equal to the length of the command arguments... ":=" expression 
                                      # allows to assign values to variables as part of an expression
                                      # So this if statement checks that there is only two arguments: python file and .txt file
    print(f"Error: One argument expected, got {args_count - 1}")
    raise SystemExit(2) # Stops the script
elif args_count < 2:
    print("Error: You must specify the name of the file")
    raise SystemExit(2) # Stops the script

FILENAME= sys.argv[1] # Argument 1 in the command line is our FILENAME. 
                      # Argument 0 is es.py

if os.path.exists(FILENAME):
    with open(FILENAME,'r') as f:
        data=f.read()
        # Count the number of e's in data
        out=data.count('e')
        print(f'The characer "e" appears a total of {out} times in the file "{FILENAME}"')
else:
    print(f'Error: File "{FILENAME}" does not exist')