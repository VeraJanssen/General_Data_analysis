# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 09:50:00 2015

@author: verajanssen
"""

import numpy as np
import matplotlib.pyplot as plt


backgate = False

if backgate == True:
    filename = '[AB]IVg_Vg_n3000_500mV_Vsd_n10mV_10mV_2'
    source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[2Dmat]Liquid_gate_mos2/2015_8_6/Measurements/chip2/DEME_TFSI/'
    IV = np.loadtxt(source_dir+filename +'.dat')
    start = -30
    end = 30
    
    size = np.shape(IV)[1]/2
    gate =  np.linspace(start, end, size) 
    bias = [-10*1e-3, -5*1e-3, 0, 5*1e-3, 10e-3]
    C_sio = 1.2e-8 #F/cm2
    L = 2.4e-6 #m
    W = 6.7e-6 #m
    mobility = np.empty(5)
    
    
    
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
    
else:
    filename = '[AB]IVg_Vg_n3000_500mV_Vsd_n10mV_10mV_2'
    source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[2Dmat]Liquid_gate_mos2/2015_8_6/Measurements/chip2/DEME_TFSI/' 
    IV = np.loadtxt(source_dir+filename +'.dat')
    start = -3.0
    end = 1.0
    
    mobility = 5.0 #cm2/Vs
    
    size = np.shape(IV)[1]/2
    gate =  np.linspace(start, end, size) 
    bias = [-10*1e-3, -5*1e-3, 0, 5*1e-3, 10e-3]
    
    L = 3e-6 #m
    W = 5.85e-6 #m
    C = np.empty(5)
    
    
    
    plt.figure()
    for i in range(np.size(IV,0)):
            plt.plot(gate, IV[i,0:size]*1e6, label=i)
            plt.xlabel('Vg(V)')
            plt.ylabel('Isd($\mu$A)')
            #plt.legend()
            print i
    
            coefficients = np.polyfit(gate[int((2.8/4.0)*size):int((3.1/4.0)*size)], IV[i, int((2.8/4.0)*size):int((3.1/4.0)*size)], 1)
            mlin = coefficients[0]
            polynomial = np.poly1d(coefficients)
            fit = polynomial(gate)
            if bias[i] != 0:
                C[i] = (mlin*L/(mobility*W*bias[i]))
            plt.plot(gate[size/2:size], fit[size/2:size]*1e6, 'k--')
            
            #Fit for the holes
            coefficients_h = np.polyfit(gate[int((0.3/4.0)*size):int((0.6/4.0)*size)], IV[i, int((0.3/4.0)*size):int((0.6/4.0)*size)], 1)
            mlin_h = coefficients_h[0]
            polynomial_h = np.poly1d(coefficients_h)
            fit_h = polynomial_h(gate)
            #if bias[i] != 0:
                #C[i] = (mobility*W*bias[i])/(mlin*L)
            plt.plot(gate[0:size/3], fit_h[0:size/3]*1e6, 'k--')
            
            
    plt.text(-0.3,-0.3,'$C_{LG}$ ='+str((C[0]))+'F/cm2')
    plt.text(-0.3,0.3,'$C_{LG}$ ='+str((C[4]))+'F/cm2')
    plt.text(-2.5, 0.35, 'mholes/melectrons = ' + str(mlin_h/mlin))
    plt.savefig(source_dir + filename + '.png')