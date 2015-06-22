# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:12:59 2015

@author: verajanssen
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:35:41 2015

@author: verajanssen
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import fnmatch



#device size
width = 16e-6       #m
length = 4e-6       #m
thickness = 6e-9    #m

#constants
e = 1.602e-19       #C
n = 2.86e12         #crystals/cm2



Vsd = (0.05, 0.025, 0,-0.025,-0.05)

IVsd = np.empty(297)
const_gate = 0
mlin = np.empty(1)



"""""""""""""Functions"""""""""""""
def make_array_IVs(source_dir, IVsd, const_gate):

    for file in os.listdir(source_dir):
        if fnmatch.fnmatch(file, '*.dat'):
            print file
            IVsdnew = np.loadtxt(source_dir + file)
            IVsd = np.column_stack((IVsd, IVsdnew[:,1]))
            const_gate = np.column_stack([const_gate, file])
    return IVsd, const_gate            
    
def plot_ivsd(bias, IVsd, file):       
    rawIVsd = plt.figure()    
    for i in range(np.size(IVsd,1)-1):
        plt.plot(bias*1e3, IVsd[:,i+1]*1e6, label=file)
    plt.xlabel('Vsd(mV)')
    plt.ylabel('Isd($\mu$A)')
    #plt.legend()
    #plt.legend('1100mV', '1200mV','1300mV','1400mV','1500mV', '1600mV','1700mV','1800mV','1900mV','2000mV')
    plt.show(rawIVsd)
    

def plot_R(bias, IVsd):   
    Rarr = np.empty(1)
    for i in range(np.size(IVsd,1)-1):
        R = 1/np.polyfit(bias,IVsd[:,i+1],1)[0]
        Rarr = np.column_stack([Rarr, R])
    plt.figure()
    plt.scatter(np.linspace(-1.1,-2,10), Rarr[0,1:11])

"Start script"

 # open IVsd files from IVsd folder
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IV2/'

IVsd, const_gate = make_array_IVs(source_dir, IVsd, const_gate)


#bias = IVsdnew[:,0] #in V   
plot_ivsd(bias, IVsd, file)


plot_R(bias, IVsd)

        
        

 # open IVg files from IVg folder
IVg = np.loadtxt('C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/IVg/megasweep2.dat') #A
gate = np.linspace(0.5, -2, np.size(IVg,1)) #V

lin_region_start = 620
lin_region_end = 680

#rawIVg = plt.figure()
plt.figure()
for i in range(np.size(IVg, 0)):
    #plt.plot(gate[lin_region_start:lin_region_end], IVg[i, lin_region_start:lin_region_end])
    #subtract the Vg = 0V (background) curve. Use the middle column. Will give error when the number of measurements is odd (than there is no Vg = 0V) 
    normIVg = IVg[i, :]-IVg[(np.size(IVg, 0)-1)/2]
    
    mlinnew = np.polyfit(gate[lin_region_start:lin_region_end], normIVg[lin_region_start:lin_region_end], 1)
    x = np.linspace(-.5, 0, 100)    
    fit = mlinnew[0]*x+mlinnew[1]
    #plt.plot(x, fit)    
    mlin = np.column_stack([mlin, mlinnew[0]]) 
    sigma = -(length*normIVg)/(width*0.25*Vsd[i])
    mobility = sigma/(e*n)

    if i==0:
        plt.plot(gate,  normIVg*1e9, label = 'Vsd = -50mV' )
    if i==1:
        plt.plot(gate, normIVg*1e9, label = 'Vsd = -25mV' )
    if i==2:
        plt.plot(gate, normIVg*1e9, label = 'Vsd = 0mV' )
    if i==3:
        plt.plot(gate, normIVg*1e9, label = 'Vsd = 25mV' )
    if i==4:
        plt.plot(gate, normIVg*1e9, label = 'Vsd = 50mV' )
    plt.title('')
    plt.xlabel('V$_{g}$ (V)')
    plt.ylabel('I(nA)')
    plt.legend(loc = 'southeast')

#Plot resistance from IVsd's




 # check for loop or seperate files

 # plot both datasets in two figures in same window

 # save the figure with foldername, filenames, githash

 # calculate mobility, Rsq