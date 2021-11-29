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

fig, ax1 = plt.subplots(constrained_layout=True)
RI1=1.52
Theta = np.arange(67,91,.1) # This is for RI 1.52.
d=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
#plt.plot(Theta, d, label="N1 RI = 1.52")
ax1.plot(Theta, d)

RI1=1.6
Theta = np.arange(61,91,.1)
d1=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
#plt.plot(Theta, d1, label="N1 RI = 1.6")
ax1.plot(Theta, d1)

ax1.set_xlabel(r'$\theta$' ' w.r.t a line perpendicular to face \n(deg)')
ax1.set_ylabel('Field Depth (nm)')
ax1.set_title('Evanescent Field Depths at Different RIs \n$\lambda_0$=637 nm')

ax2=ax1.twiny()
ax2.set_xlim(ax1.get_xlim()) # ensure the independant x-axes now span the same range
ax2.set_xticks(Theta) # copy over the locations of the x-ticks from the first axes
ax2.set_xticklabels(90-Theta) # But give them a different meaning
#newlabel=[90-Theta]

#ax2.set_xlabel('Angle w.r.t. chemistry surface')
#newlabel=[30, 25, 20, 15, 10, 5, 0]
#angle= 90-Theta
#Newpos=[angle(Theta) for Theta in newlabel]
#ax2.set_xlim(ax1.get_xlim())

# def a(Theta):
#     return 90-Theta

# def b(Theta):
#     return 1/(90-Theta)

# secax = ax.secondary_xaxis('top', functions=(a, b))


# RI1=1.65
# Theta = np.arange(58,91,.1)
# d2=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
# plt.plot(Theta, d2, label="N1 RI = 1.65")

# RI1=1.7
# Theta = np.arange(55.4,91,.1)
# d3=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
# plt.plot(Theta, d3, label="N1 RI = 1.7")

# RI1=1.78
# Theta = np.arange(51.8,91,.1)
# d4=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
# plt.plot(Theta, d4, label="N1 RI = 1.78")

# RI1=1.8
# Theta = np.arange(51,91,.1)
# d5=Lambda/(4*math.pi)*((RI1**2*(np.sin(np.radians(Theta))**2)-RI2**2)**-0.5)
# plt.plot(Theta, d5, label="N1 RI = 1.8")


# Preparing graph title, legend, labels, and equation
#plt.title('Evanescent Field Depths at Different RIs \n$\lambda_0$=637 nm')
#plt.xlabel(r'$\theta$' ' w.r.t a line perpendicular to face \n(deg)')
#plt.ylabel('Field Depth (nm)')
#plt.legend(bbox_to_anchor=(1.15, 1)) # first value is x, 2nd =y, set >1 to put outside
# see https://www.delftstack.com/howto/matplotlib/how-to-place-legend-outside-of-the-plot-in-matplotlib/
plt.legend()

# fig, ax = plt.subplots(constrained_layout=True)
# ax.plot(Theta, d)
# ax.set_xlabel('angle [degrees]')
# ax.set_ylabel('signal')
# ax.set_title('Sine wave')


# plt.text(50,42,'d=' r'$\frac{\lambda_0}{4\pi}$' r'$[n^{2}_{1}sin^{2}\theta-n^{2}_{1}]^{-1/2}$')

#secaxx = ax.secondary_xaxis('top', functions=(90-x))

plt.show()

# *** de-comment to save out. Change extension to .svg for vector ***
#plt.savefig('plot.png', dpi=400)