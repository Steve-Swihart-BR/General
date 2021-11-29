# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:55:54 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import numpy as np

plt.style.use('xkcd')
#plt.style.use('seaborn-darkgrid')



x = np.arange(0,10,.1)
y=(np.sin(x))
z=2*(np.sin(x))
#fig, ax = plt.subplots(1,1)
#ax.plot(x,y)
plt.plot(x,y, label="pointless")
plt.plot(x,z, label="also pointless")
plt.title("yo")
plt.xlabel('X marks this axis \nnot another')
plt.ylabel('icky')
plt.legend()
plt.show()
