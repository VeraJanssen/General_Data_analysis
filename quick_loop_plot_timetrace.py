# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:36:27 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt


filename = 'IVg_Vg_n500mV_0_Vsd_n10mV[rev]10x'
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements_square_lattices/Liquid_gate/9_14_150828_62/stability/' 
IV = np.loadtxt(source_dir+filename +'.dat')
start = 0
end = 1

size = np.shape(IV)[1]
bias =  np.linspace(start, end, size) 



plt.figure()
for i in range(np.size(IV,0)):
        plt.plot(bias+(i), IV[i,0:size]*1e9, label=i)
        plt.xlabel('time(s)')
        plt.ylabel('Isd(nA)')
        #plt.legend()
        print i
        
plt.savefig(source_dir + filename + '.png')