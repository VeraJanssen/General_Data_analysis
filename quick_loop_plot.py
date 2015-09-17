# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:36:27 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt


filename = 'IIVs_Vg_0V_n500mV_Vsd_n10mV_10mV_afternight'
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements_square_lattices/Liquid_gate/9_14_150828_62/stability/' 
IV = np.loadtxt(source_dir+filename +'.dat')
start = -10
end = 10
fit = np.empty(np.size(IV,0))

size = np.shape(IV)[1]
bias =  np.linspace(end, start, (size/2)+1) 



plt.figure()
for i in range(np.size(IV,0)):
        plt.plot(bias, IV[i,size/2:size]*1e9, label=i)
        plt.xlabel('Vsd(mV)')
        plt.ylabel('Isd(nA)')
        #plt.legend('nr:')
        print i
        plt.text(-9,0.4, filename)
        
        fit[i] = np.polyfit(bias, IV[i, size/2:size], 1)[0]

        
plt.savefig(source_dir + filename + 'n500mV_1000mV' + '.png')


plt.figure()
plt.scatter(np.linspace(0, -500, 6), fit)