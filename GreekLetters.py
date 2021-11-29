# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 18:45:50 2020

@author: Steve
"""
import matplotlib as mpl
#mpl.rcParams['text.usetex'] = True
#mpl.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}'] #for \text command
mpl.rcParams['text.usetex'] = False

print(r"$f_{\mathrm{cor, r}}$")

x = range(945,970,1)
for y in x:
    print(y, chr(y))
#greek_letterz=[chr(code) for code in range(945,970)]
#print(greek_letterz)