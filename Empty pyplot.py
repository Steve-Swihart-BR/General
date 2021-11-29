# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:44:40 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-darkgrid') # commenting will make plot pure white.

# x = np.arange(0, 10, 0.2)
# y = np.sin(x)
fig, ax = plt.subplots(facecolor='#dcdcdc')
# ax.plot(x, y)

plt.title('Evanescent Field Depths at Different RIs \n$\lambda_0$=637 nm', pad=27)
plt.xlabel(r'$\theta$' ' w.r.t a line perpendicular to face \n(deg)')
plt.ylabel('Field Depth (nm)')
plt.show()