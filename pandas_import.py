# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:14:11 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import csv
import pandas as pd

data = pd.read_csv('csvfile1.txt')

x = []
y = []

with open('csvfile1.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(data)  #comment if don't need. Good way to know data got imported.

        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.text(x=4.2, y=130, s='Sources: the interwebs', color='#524939')  # can incl horizontalalignment='left'
plt.show()