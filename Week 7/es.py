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
@Desc    :   Weekly Task 7. Reading a file and output the number of e's it contains
'''

import os #import package os
import sys #import package sys

# Idea and process flow on how to do it from: https://realpython.com/command-line-interfaces-python-argparse/

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

# Now, we will check that the FILENAME path exists! To do so, we will use the try:, except functions we see later in the course
try: 
    with open(FILENAME,'r') as f: #read the file.name and call it f. With statement closes the file for us "https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/"
        out=f.read().count('e') #Read f and count the number of "e's" it contains. Assign to object out to print it later
        print(f'The character "e" appears a total of {out} times in the file "{FILENAME}"')
except OSError as e: #If the filename does not exist, raise a file or directory error. Info taken: https://www.topbug.net/blog/2020/10/03/catching-filenotfounderror-watch-out/
    print(e) #Print the error
    sys.exit(1) #Stops the programme

