# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:36:27 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt


source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[2Dmat]Liquid_gate_mos2/Device2/Measurements/Chip2/Dev1/[IVsweep]IVsdn100mV_100mV_Vgn30V_30V.dat'

IV = np.loadtxt(source_dir)

bias =  np.linspace(-0.1, 0.1, 1191)

for i in range(np.size(IV,1)-1):
        plt.plot(IV[i,0:np.size(IV[i,:])/2]*1e6, label=file)
        plt.xlabel('Vsd(mV)')
        plt.ylabel('Isd($\mu$A)')