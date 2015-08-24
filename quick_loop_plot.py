# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:36:27 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt


filename = '[AB]IVg_Vg_n3000_500mV_Vsd_n10mV_10mV_2'
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[2Dmat]Liquid_gate_mos2/2015_8_6/Measurements/chip2/DEME_TFSI/' 
IV = np.loadtxt(source_dir+filename +'.dat')
start = -3
end = 1

size = np.shape(IV)[1]
bias =  np.append(np.linspace(start, end, size/2, endpoint=False), np.linspace(end, start, (size/2))) 



plt.figure()
for i in range(np.size(IV,0)):
        plt.plot(bias, IV[i,:]*1e6, label=i)
        plt.xlabel('Vg(V)')
        plt.ylabel('Isd($\mu$A)')
        #plt.legend()
        print i
        
plt.savefig(source_dir + filename + '.png')