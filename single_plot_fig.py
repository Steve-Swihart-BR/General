# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:16:28 2020

@author: Steve
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 12:00:20 2020

@author: Steve
"""


#import matplotlib
import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
fig, ax = plt.subplots(facecolor='#cccccc')  #'lightslategrey' is nice but dark
plt.style.use('seaborn-darkgrid')
#axes= fig.add_axes([0.1,0.1,0.8,0.8])
# axes.set_facecolor('#5f5f5f')   #to override plt.style




# Preparing graph title, legend, labels, and equation
plt.title('Evanescent Field Depths at Different RIs \n$\lambda_0$=637 nm')
plt.xlabel(r'$\theta$' ' w.r.t a line perpendicular to face \n(deg)')
plt.ylabel('Field Depth (nm)')
#plt.legend(bbox_to_anchor=(1.15, 1)) # first value is x, 2nd =y, set >1 to put outside
# see https://www.delftstack.com/howto/matplotlib/how-to-place-legend-outside-of-the-plot-in-matplotlib/
plt.legend()

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



fig.show()