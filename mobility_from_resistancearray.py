# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:48:03 2015

@author: Vera
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import fnmatch

mobility =  np.empty(15) 
mlin = np.empty(15)
i = 0
C_LG = 1e-7 # assumption from DEME-TFSI on MoS2
dimensions = {}
dimensions['sd'] = [25.0,5.0]
dimensions['s1'] = [13.0,1.0]
dimensions['s2'] = [13.0,3.5]
dimensions['s3'] = [16.3,3.5]
dimensions['s4'] = [8.2,1.0]
dimensions['d1'] = [13.0,3.5]
dimensions['d2'] = [21.0,1.0]
dimensions['d3'] = [16.3,1.0]
dimensions['d4'] = [8.2,3.5]
dimensions['12'] = [13.0,2.0]
dimensions['34'] = [8.2,2.0]
dimensions['14'] = [0.5,8.5]
dimensions['23'] = [0.5,8.5]

mobility = {}

source_dir = 'C:/Users/Vera/surfdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements_square_lattices/Liquid_gate/9_17_150828_63/devE/' 
for file in os.listdir(source_dir):
    if fnmatch.fnmatch(file, '*.npy'):
        filename =  file
        try:
            W,L = dimensions[filename[2]+filename[1]]   
            
        except KeyError:
            W,L = dimensions[filename[1]+filename[2]]
            
        R = np.load(source_dir + file)
        I_sd = 0.01/R
        plt.figure()        
        plt.scatter(np.linspace(0,-0.500, 6), I_sd*1e9)
        fit = np.polyfit(np.linspace(0,-0.500, 6), I_sd[0:6], 1)
        mlin[i] = fit[0]  
        p = np.poly1d(fit)
        plt.plot(np.linspace(0, -0.5,100), p(np.linspace(-0.1, -0.5,100))*1e9)
        mobility[filename[1:3]] = np.abs(mlin[i]*(L/W)*(1/(0.01*C_LG)))
    
        i=i+1
