# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:50:00 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt

filename = '[13]IVg_Vg_n30_30V_Vsd_n10mV_10mV'
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[2Dmat]Liquid_gate_mos2/2015_8_6/Measurements/chip3/' 
IV = np.loadtxt(source_dir+filename +'.dat')
start = -30
end = 30

size = np.shape(IV)[1]/2
gate =  np.linspace(start, end, size) 
bias = [-10*1e-3, 0, 10e-3]
C_sio = 1.2e-8 #F/cm2
L = 2.4e-6 #m
W = 6.7e-6 #m
mobility = np.empty(3)



plt.figure()
for i in range(np.size(IV,0)):
        plt.plot(gate, IV[i,0:size]*1e6, label=i)
        plt.xlabel('Vg(V)')
        plt.ylabel('Isd($\mu$A)')
        #plt.legend()
        print i

        coefficients = np.polyfit(gate[int((10.7/40.0)*size):int((22.0/40.0)*size)], IV[i, int((10.7/40.0)*size):int((22.0/40.0)*size)], 1)
        mlin = coefficients[0]
        polynomial = np.poly1d(coefficients)
        fit = polynomial(gate)
        if bias[i] != 0:
            mobility[i] = mlin*(L/W)*(1/(bias[i]*C_sio)) 
        plt.plot(gate, fit*1e6)
plt.text(-15,-0.04,'$\mu_{FE}$ ='+str(round(mobility[0]))+'cm$^{2}$/Vs')
plt.text(-15,0.04,'$\mu_{FE}$ ='+str(round(mobility[2]))+'cm$^{2}$/Vs')
plt.savefig(source_dir + filename + '.png')