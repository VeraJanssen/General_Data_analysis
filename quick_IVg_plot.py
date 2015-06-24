# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:40:46 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt

#device size
width = 16e-6       #m
length = 4e-6       #m
thickness = 6e-9    #m


#constants
e = 1.602e-19       #C
n = 2.86e12         #crystals/cm2

source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/'

highsd = np.loadtxt(source_dir +'Vb50mV.dat')
zerosd = np.loadtxt(source_dir +'Vb0mV.dat')
lowsd  = np.loadtxt(source_dir +'Vbn50mV.dat')

plt.figure()
plt.plot(highsd[:,0], highsd[:,1]*1e6, label = 'V$_{bias}$ = 50mV')
plt.plot(zerosd[:,0], zerosd[:,1]*1e6, label = 'V$_{bias}$ = 0mV')
plt.plot(lowsd[:,0], lowsd[:,1]*1e6, label = 'V$_{bias}$ = -50mV')
plt.legend()
plt.xlabel('V$_g$(V)')
plt.ylabel('I$_{sd}$($\mu$A)')

plt.savefig(source_dir + 'quick_IVg.png')


plt.figure()
sigmah = (length*highsd[:,1])/(width*0.05)
mobilityh = sigma/(e*n)     


sigmaz = (length*zerosd[:,1])/(width*0.0)
mobilityz = sigmaz/(e*n)    

sigmal = (length*lowsd[:,1])/(width*-0.05)
mobilityl = sigmal/(e*n)    

 
plt.plot(highsd[:,0],mobilityh)
plt.plot(zerosd[:,0],mobilityz)
plt.plot(lowsd[:,0], mobilityl)
plt.legend()
plt.xlabel('V$_g$(V)')
plt.ylabel('mobility(cm$^2$/Vs)')


plt.savefig(source_dir + 'mobility_quick_scan.png')