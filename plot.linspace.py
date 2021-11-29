# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:09:05 2020

@author: Steve
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


plt.style.use('seaborn')


x = np.linspace(0, 2, 100)

plt.plot(x, x, label='supposedly linear')
plt.plot(x, x**2, label='maybe quadratic')
plt.plot(x, x**3, label='definitely cubic')

plt.xlabel('I wonder what x label \ncould be')
plt.ylabel('y \nlabel')

plt.title("Pointless Plot")

plt.legend()


plt.show()
