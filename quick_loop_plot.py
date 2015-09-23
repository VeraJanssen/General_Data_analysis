# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:36:27 2015

@author: verajanssen
Plots and saves IVs in a folder. Works with IV_loop labview routine. To do: implement the standart size of the sample from txt file to calculate the sheet resistance 
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import fnmatch

save = False
W = 0.5 #um
L = 8.5 #um
start_bias = -10 #mV
end_bias = 10 #mV
start_gate = 0 #mV
end_gate = 500 #mV

class props:
    DIM = [[25,5], [13,1], [13,3.5], [16.3, 3.5], [8.2,1], [13,3.5], [21,1], [16.3,1], [8.2, 3.5], [13,2], [8.2,2],[0.5,8.5],[0.5,8.5]]
        

def plot_IV(IV, filename, bias, size):
    plt.figure()
    for i in range(np.size(IV,0)):
        plt.plot(bias, IV[i,size/2:size]*1e9, label=i)
        plt.xlabel('Vsd(mV)')
        plt.ylabel('Isd(nA)')
        plt.text(-9,0.4, filename)
        R[i] = 1/np.polyfit(bias*1e-3, IV[i, size/2:size], 1)[0]
        W,L = props.DIM[i]
        Rs[i] = R[i]*(W/L) #not working: needs the proper sizes, not implemented yet
        if save:                        
                plt.savefig(source_dir + filename + '.png')
        plt.close()
        return R, Rs

def plot_R(R,Rs, start_gate, end_gate, nr_gate):        
    plt.figure()
    plt.scatter(np.linspace(start_gate, end_gate, nr_gate), R*1e-6)
    plt.xlabel('Vg(mV)')
    plt.ylabel('R(M$\Omega$)')
    plt.savefig(source_dir +filename + '[R]' + '.png')
    if save:
        np.save(source_dir+filename, R)
    plt.close()
    
        
source_dir = 'C:/Users/Vera/surfdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements_square_lattices/Liquid_gate/9_17_150828_63/devE/' 
for file in os.listdir(source_dir):
    if fnmatch.fnmatch(file, '*.dat'):
        filename =  file
        print filename
        dev = 'Hallbar53.'+filename[1:3]
        IV = np.loadtxt(source_dir + file)
        R = np.empty(np.size(IV,0)) #Ohm
        Rs = np.empty(np.size(IV,0)) #Ohm/sq
        nr_gate = np.shape(IV)[0]
        size = np.shape(IV)[0]
        bias =  np.linspace(end_bias, start_bias, (size/2))  #mV
        
        
        R, Rs = plot_IV(IV, filename, bias, size)

        plot_R(R,Rs, start_gate, end_gate, nr_gate)
