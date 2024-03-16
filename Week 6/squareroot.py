#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   squareroot.py
@Time    :   2024/03/09 00:04:49
@Author  :   Guillermo Martin
@Version :   1.0
@Personal email : gfmg1992@hotmail.com
@Student email: G00438885@atu.ie
@License :   (C)Copyright 2023, Guillermo Martin
@Desc    :   Perform square root based on the Newton method
Formula from the newton method found: 
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
'''

def sqrt(l= 0.0001): # N: positive integer to calculate square root
                        # l: the so called "tolerance limit". Default value 0.0001
    while True: 
        try:
            N = int(input("Enter the number you want the square root of: "))  
            if N < 0: #Check the input is positive, otherwise ask for a number again
                print("Please enter a non-negative number")
                continue
            break #Breaks above while loop
        except ValueError:
            print("That was not a number. Please enter a number.")
    
    x = N #Define a new parameter x..As in newton formula

    count = 0 #To keep track of the amount of loops to reach solution
 
    while (1) : #Infinite loop until tolerace limit is achieve
        count += 1 #Update loop count
        print(f"Iteration {count}")

        if (N== 0): #Root squared of 0 is 0, Newton formula does not work
            root=0
        else:    
            # Newton root formula
            root = 0.5 * (x + (N / x)) 
 
        #Once the difference between the root calculated value
        # and x is less than the tolerance limit, 
        # we finalize the function
        if (abs(root - x) < l) : 
            print(f"The square root of {N} is ~{round(root,2)}")
            return root 
            break
 
        # If the above if statement is not achieved, we update the while loop 
        x = root
    
sqrt()    