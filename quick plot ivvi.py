# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:25:45 2015

@author: verajanssen
"""

#iv.vi plots

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import fnmatch

source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[2Dmat]Liquid_gate_mos2/Device4/Measurements/DevC/LIQUID/IVg_2/'


for file in os.listdir(source_dir):
    if fnmatch.fnmatch(file, '*.dat'):
        print file
        IV = np.loadtxt(source_dir + file)
        plt.plot(IV[:,0], IV[:,1]*1e6, label=file)
        plt.xlabel('Vg(V)')
        plt.ylabel('Isd($\mu$I)')
       # plt.show()
plt.legend(loc=2)        
plt.show()