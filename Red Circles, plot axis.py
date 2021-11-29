# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 16:41:36 2020

@author: Steve
"""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') #r=red, o=circle
# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.axis([0, 6, 0, 18]) #x start, x end, y start, y end
#plt.axis (xmax=5)
plt.show()