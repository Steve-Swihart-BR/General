# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:38:51 2020

@author: Steve
"""

# Plot Planner Tool is here
#    https://qed0711.github.io/plot-planner/
#
# and description is here
#   https://towardsdatascience.com/subplots-in-matplotlib-a-guide-and-tool-for-planning-your-plots-7d63fa632857 
#

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,8))
ax1 = plt.subplot2grid((3, 2), (0, 0), rowspan=1, colspan=1, xticklabels=[], yticklabels=[], xticks=[], yticks=[], fc="red",)
ax2 = plt.subplot2grid((3, 2), (1, 0), rowspan=2, colspan=1, xticklabels=[], yticklabels=[], xticks=[], yticks=[], fc="blue",)
ax3 = plt.subplot2grid((3, 2), (0, 1), rowspan=3, colspan=1, xticklabels=[], yticklabels=[], xticks=[], yticks=[], fc="orange",)

ax1.text(0.5, 0.5, "ax1 \n(rows = 2/3)", horizontalalignment='center', verticalalignment='center')
ax2.text(0.5, 0.5, "ax2", horizontalalignment='center', verticalalignment='center')
ax3.text(0.5, 0.5, "ax3", horizontalalignment='center', verticalalignment='center')


plt.show()