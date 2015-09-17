# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:36:27 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt


filename = 'IVg_Vg_n500V_2000mV_Vsd_n10mV_globalde_1000us'
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements_square_lattices/Liquid_gate/9_14_150828_62/stability/' 
IV = np.loadtxt(source_dir+filename +'.dat')
start = 0
end = 6

size = np.shape(IV)[1]
bias =  np.linspace(start, end, size) 



plt.figure()
for i in range(np.size(IV,0)):
        plt.plot(bias+(i*end), IV[i,0:size]*1e9, label=i)
        plt.xlabel('time(min)')
        plt.ylabel('Isd(nA)')
        #plt.legend()
        plt.text(5,0.51,filename)
        print i
        
plt.savefig(source_dir + filename + '.png')