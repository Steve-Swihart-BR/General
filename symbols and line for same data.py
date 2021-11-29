# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:05:21 2020

@author: Steve
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.01)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# to do with same color, just add - to first plot, remove 2nd, so:
# plt.plot(t1, f(t1), 'bo-')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

plt.show()