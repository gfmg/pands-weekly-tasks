#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   plottask.py
@Time    :   2024/03/16 19:42:13
@Author  :   Guillermo Martin
@Version :   1.0
@Personal email : gfmg1992@hotmail.com
@Student email: G00438885@atu.ie
@License :   (C)Copyright 2023, Guillermo Martin
@Desc    :   Weekly task 8
'''

import numpy as np
import matplotlib.pyplot as plt

# Default fonts for the title, x and y axis
fontdtitle = {'color':'black','size':20,'weight':'bold'}
fontx = {'color':'black','size':12,'weight':'bold'}
fonty = {'color':'black','size':12,'weight':'bold'}

# A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
dat = np.random.normal(loc=5,scale=2,size=1000)

plt.figure(figsize = (5, 5))
plt.hist(dat,color="blue",edgecolor="black")
plt.axvline(x=dat.mean(),color="red",linestyle='dashed') #plot vertical line as the mean
# Following lines are plot formatting
plt.title("A random normal sample",  fontdict = fontdtitle)
plt.ylabel('Y',fontdict = fontx)
plt.xlabel('X',fontdict = fonty)
min_ylim, max_ylim = plt.ylim()
plt.text(x=dat.mean()*1.1, y=max_ylim*0.95, s='Mean: {:.5f}'.format(dat.mean()),color="red",size=12)
plt.show()

# And a plot of the function  h(x)=x3 in the range 0 to 10, 
x = np.array(np.arange(0,10,0.2)) #numpy range function to define numbers as floats
y = x ** 3

plt.figure(figsize = (5, 5))
plt.plot(x,y,label="$Y: x^3$")
#Following lines are plot formatting
plt.title("Cubic function",  fontdict = fontdtitle)
plt.ylabel('Y',fontdict = fontx)
plt.xlabel('X',fontdict = fonty)
plt.legend()
plt.show()