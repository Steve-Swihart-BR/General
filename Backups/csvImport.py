# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:14:11 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('csvfile1.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(plots)
#fig, ax1=plt.subplots()
#rects=ax1.bar

        x.append(int(row[0]))
        y.append(int(row[1]))
        
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()