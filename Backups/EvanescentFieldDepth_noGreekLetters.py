# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:31:10 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

plt.style.use('seaborn-darkgrid')
plt.rcParams.update({'font.size': 9})
mpl.rc('lines', linewidth=2.0)  # need import as mpl above. 
#                               This is global for all plots in this file
#                               can override with ",linewidth=2" at end of plt.plot

Lambda=637.0
Theta=72

#Use substrate RI by setting RI1 to what you want. 
#   1.52, 1.6, 1.65, 1.7, 1.78, 1.8
RI1=1.52

RI2 = 1.33 #water/oil

# *** Formula for evanescent field penetration depth***
#    see this http://light.ece.illinois.edu/ECE564/Research_Projects_files/Tirf_review.pdf
#    or this https://docs.google.com/spreadsheets/d/10HGHz56A5p7LdRymXTpIU4L4chKY9TeK59xhUHG0v_g/edit#gid=0
# ******************************
#
# d = Lambda/4pi(n1^2sin^2Theta-N2^2)^-0.5

Theta = np.arange(67,91,.1) # This is for RI 1.52.
d=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)

plt.plot(Theta, d, label="N1 RI = 1.52")

RI1=1.6
Theta = np.arange(61,91,.1)
d1=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
plt.plot(Theta, d1, label="N1 RI = 1.6")

RI1=1.65
Theta = np.arange(58,91,.1)
d2=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
plt.plot(Theta, d2, label="N1 RI = 1.65")

RI1=1.7
Theta = np.arange(55.4,91,.1)
d3=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
plt.plot(Theta, d3, label="N1 RI = 1.7")

RI1=1.78
Theta = np.arange(51.8,91,.1)
d4=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
plt.plot(Theta, d4, label="N1 RI = 1.78")

RI1=1.8
Theta = np.arange(51,91,.1)
d5=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
plt.plot(Theta, d5, label="N1 RI = 1.8")

plt.title("Evanescent Field Depths \nat Different RIs")
plt.xlabel('Theta \nw.r.t a line perpendicular to face')
plt.ylabel('Field Depth (nm)')
plt.legend()
plt.show()