# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:00:20 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(nrows=2, ncols=2) #row, col, starting upper left
axes[0,0].set_title('upper left')
axes[1,1].set_title('lower right')
figure.suptitle("Main Title")

figure.tight_layout()
# tight_layout automatically adjusts subplot params so that the subplot(s) 
# fits in to the figure area.

plt.show()