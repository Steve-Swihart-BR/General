# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:00:20 2020

@author: Steve
"""


#import matplotlib
import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(nrows=2, ncols=2) #row, col, starting upper left

plt.style.use('seaborn-darkgrid')



axes[0,0].set_title('upper left')
axes[0,0].set_facecolor('xkcd:mint green')

axes[1,1].set_title('lower right', fontsize=9)




figure.suptitle("Main Title of significant length")  #or plt.suptitle

plt.subplots_adjust(bottom=0, wspace=0.2, hspace=.3)
# The parameter meanings (and suggested defaults) are:
#
# left  = 0.125  # the left side of the subplots of the figure
# right = 0.9    # the right side of the subplots of the figure
# bottom = 0.1   # the bottom of the subplots of the figure
# top = 0.9      # the top of the subplots of the figure
# wspace = 0.2   # the amount of width reserved for blank space between subplots (horizontal)
# hspace = 0.2   # the amount of height reserved for white space between subplots (vertical)


#plt.rc('patch', edgecolor='#60606') #grey subplot background
#plt.rc('grid', color='w', linestyle='solid')  #white gridlines
#plt.rc('patch', facecolor='#E0E0E0')
#figure.set_tight_layout(True) #call tight_layout every time

# figure.tight_layout() #without this lower row titles interfere with upper row axis labels
# ight_layout automatically adjusts subplot params so that the subplot(s) 
# fits in to the figure area.

plt.show()