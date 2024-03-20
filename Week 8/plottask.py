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

# Grid for plots
fig, axs = plt.subplots(2, figsize=(7, 7))

# A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
dat = np.random.normal(loc=5,scale=2,size=1000)

#axs[0].figure(figsize = (5, 5))
axs[0].hist(dat,color="blue",edgecolor="black")
axs[0].axvline(x=dat.mean(),color="red",linestyle='dashed',label='Mean: {:.5f}'.format(dat.mean())) #plot vertical line as the mean
# Following lines are plot formatting
axs[0].set_title("A random normal sample",  fontdict = fontdtitle)
axs[0].set_ylabel('Y',fontdict = fontx)
axs[0].set_xlabel('X',fontdict = fonty)
axs[0].legend()
min_ylim, max_ylim = axs[0].set_ylim()
#axs[0].text(x=dat.mean()*1.1, y=max_ylim*0.95, s='Mean: {:.5f}'.format(dat.mean()),color="red",size=12)

# And a plot of the function  h(x)=x3 in the range 0 to 10, 
x = np.array(np.arange(0,10,0.2)) #numpy range function to define numbers as floats
y = x ** 3

axs[1].plot(x,y,label="$Y: x^3$")
#Following lines are plot formatting
axs[1].set_title("Cubic function",  fontdict = fontdtitle)
axs[1].set_ylabel('Y',fontdict = fontx)
axs[1].set_xlabel('X',fontdict = fonty)
axs[1].legend()


plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9, hspace=0.4)

plt.show()
