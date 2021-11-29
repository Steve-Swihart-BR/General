# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:31:10 2020

@author: Steve
"""


import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import math

# style and overrides of it
plt.style.use('seaborn-darkgrid')
plt.rcParams.update({'font.size': 9})
mpl.rcParams['figure.dpi'] = 300 #needed to increase resolution
mpl.rc('lines', linewidth=2.0)  # need import as mpl above. 
#                               This is global for all plots in this file
#                               can override with ",linewidth=2" at end of plt.plot
#mpl.rcParams['text.usetex'] = False

# Fixed values (just wavelength and RI2)
Lambda=637.0
RI2 = 1.33 #water/oil
#Theta=72 used when testing equation without range.

#Use substrate RI by setting RI1 to what you want. 
#   1.52, 1.6, 1.65, 1.7, 1.78, 1.8


# *** Formula for evanescent field penetration depth***
#    see this http://light.ece.illinois.edu/ECE564/Research_Projects_files/Tirf_review.pdf
#    or this https://docs.google.com/spreadsheets/d/10HGHz56A5p7LdRymXTpIU4L4chKY9TeK59xhUHG0v_g/edit#gid=0
# ******************************
#
# d = Lambda/4pi(n1^2sin^2Theta-N2^2)^-0.5


RI1=1.52
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


# Preparing graph title, legend, labels, and equation
plt.title('Evanescent Field Depths at Different RIs \n$\lambda_0$=637 nm', pad=27)
plt.xlabel(r'$\theta$' ' w.r.t a line perpendicular to face \n(deg)')
plt.ylabel('Field Depth (nm)')
#plt.legend(bbox_to_anchor=(1.15, 1)) # first value is x, 2nd =y, set >1 to put outside
# see https://www.delftstack.com/howto/matplotlib/how-to-place-legend-outside-of-the-plot-in-matplotlib/
plt.legend()

# adding 2nd axis, angle w.r.t. chem surface, which is 90-Theta
plt.text(50,42,'d=' r'$\frac{\lambda_0}{4\pi}$' r'$[n^{2}_{1}sin^{2}\theta-n^{2}_{1}]^{-1/2}$')
plt.text(49.7,121, '40', color="#6030ff")
plt.text(54.7,121, '35', color="#6030ff")
plt.text(59.7,121, '30', color="#6030ff")
plt.text(64.7,121, '25', color="#6030ff")
plt.text(69.7,121, '20', color="#6030ff")
plt.text(74.7,121, '15', color="#6030ff")
plt.text(79.7,121, '10', color="#6030ff")
plt.text(84.7,121, '5', color="#6030ff")
plt.text(89.7,121, '0', color="#6030ff")
plt.text(70, 123.8, r'$\angle$ w.r.t chemistry surface', ha='center', fontsize='10', color="#6030ff")

plt.show()

# *** de-comment to save out. Change extension to .svg for vector ***
#plt.savefig('plot.png', dpi=400)