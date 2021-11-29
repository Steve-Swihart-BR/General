# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:00:20 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(nrows=2, ncols=2) #row, col, starting upper left

plt.style.use('seaborn-darkgrid')


axes[0,0].set_title('upper left')
axes[0,0].set_facecolor('xkcd:mint green')

axes[1,1].set_title('lower right', fontsize=9)
axes[1,1].set_facecolor('#5f5f5f')

figure.suptitle("Main Title of significant length")


#plt.rc('patch', edgecolor='#60606') #grey subplot background
#plt.rc('grid', color='w', linestyle='solid')  #white gridlines
#plt.rc('patch', facecolor='#E0E0E0')
fig.set_tight_layout(True) #call tight_layout every time
figure.tight_layout() #without this lower row titles interfere with upper row axis labels
# tight_layout automatically adjusts subplot params so that the subplot(s) 
# fits in to the figure area.

plt.show()