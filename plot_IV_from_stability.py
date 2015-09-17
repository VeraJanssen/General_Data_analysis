# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 12:58:35 2015

@author: verajanssen
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import fnmatch


source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements_square_lattices/Liquid_gate/Sample_6_7_2015_13/'
filename = '192047_[HA]IVs_Vb-10mV_Vg0V_B0T'
R = []

data = np.loadtxt(source_dir + filename + '.dat')

data2 = np.loadtxt(source_dir + '172434_IVs_Vb-10mV_Vg0V_B0T' + '.dat')

Vg = np.linspace(0, -1, 6)

Vg2 = np.linspace(0 , 2.5, 11)

plt.figure()
for n in range(6):
    V = data[(n)*(1206/6):(n+1)*(1206/6),1]

    print n
    I = data[(n)*(1206/6):(n+1)*(1206/6),2]
    plt.plot(V,I, label='Vg=%dmV'%(Vg[n]*1000))#+str(Vg[n])
    fit = np.polyfit(I*(1e-9), V*(1e-3), 1)
    R.append(fit[0])
plt.legend(loc=4)
plt.xlabel('Vbias(mV)')
plt.ylabel('Isd(nA)')
plt.show()

for n in range(11):
    V2 = data2[(n)*(2211/11):(n+1)*(2211/11),1]
    I2 = data2[(n)*(2211/11):(n+1)*(2211/11),2]
    fit = np.polyfit(I*(1e-9), V*(1e-3), 1)
    R.append(fit[0])

plt.figure()
plt.scatter(np.linspace(-1, 2.5, np.size(R)), R)
plt.xlabel('Vg')
plt.ylabel('R($\Omega$)')
 
