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

#settings
source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements square lattices/Liquid gate/20-5/'
save_figs = False

#device size
width = 16e-6       #m
length = 4e-6       #m
thickness = 6e-9    #m


#constants
e = 1.602e-19       #C
n = 2.86e12         #crystals/cm2



Vsd = (-0.05, -0.025, 0, 0.025, 0.05) #V

IVsd = np.empty(297)
normIVg = np.empty(744)
const_gate = 0
mlin = np.empty(1)
Rarr = np.empty(10)



"""""""""""""Functions"""""""""""""
def make_array_IVs(source_dir, IVsd, const_gate):

    for file in os.listdir(source_dir + 'IV2/'):
        if fnmatch.fnmatch(file, '*.dat'):
            IVsdnew = np.loadtxt(source_dir + 'IV2/' + file)
            IVsd = np.column_stack((IVsd, IVsdnew[:,1]))
            const_gate = np.column_stack([const_gate, file])
    return IVsd, const_gate            
    
def plot_ivsd(bias, IVsd, file, save_fig):       
    plt.figure()    
    for i in range(np.size(IVsd,1)-1):
        plt.plot(bias*1e3, IVsd[:,i+1]*1e6, label=file)
    plt.xlabel('Vsd(mV)')
    plt.ylabel('Isd($\mu$A)')
    #plt.legend()
    #plt.legend('1100mV', '1200mV','1300mV','1400mV','1500mV', '1600mV','1700mV','1800mV','1900mV','2000mV')
    if save_fig:
        plt.savefig(source_dir + 'ivsd.png')
    

def plot_R(bias, IVsd, Rarr, width, length, save_fig):   
    #Rarr = 0
    for i in range(np.size(IVsd,1)-1):
        R = (1/np.polyfit(bias,IVsd[:,i+1],1)[0])*(width/length) #sheet resistance
       
        Rarr[i] = R#np.column_stack([Rarr, R])
    plt.figure()
    plt.scatter(np.linspace(-1.1,-2,10), Rarr)
    plt.xlabel('V$_{g}$(V)')
    plt.ylabel('resistance ($\Omega$ / square)')
    plt.figtext(0.2,0.8,'lowest resistance: '+ str(min(Rarr)) + '$ \Omega$ / square  ' ) #sheet resistance
    if save_fig:
        plt.savefig(source_dir + 'shresistance.png')
        
        
def plot_IVg(IVg, normIVg, length, width, save_fig):
    IVg = np.loadtxt(source_dir + 'IVg/megasweep2.dat') #A
    gate = np.linspace(0.5, -2, np.size(IVg,1)) #V
    f, (raw, norm) = plt.subplots(2, 1, sharey=True)    
    for i in range(np.size(IVg, 0)):
        norma = IVg[i, :]-IVg[(np.size(IVg, 0)-1)/2]    
        #subtract the Vg = 0V (background) curve. Use the middle column. Will give error when the number of measurements is odd (than there is no Vg = 0V) 
        normIVg = np.column_stack((normIVg, norma))

    
        raw.plot(gate, IVg[i,:]*1e9)

        norm.plot(gate, norma *1e9)
        plt.title('')
        plt.xlabel('V$_{g}$ (V)')
        plt.ylabel('I(nA)')
        norm.legend(loc = 'southeast')

    if save_fig:
        plt.savefig(source_dir + 'IVg.png')
            
    return normIVg[:,1:6]
    
def plot_mobility(normIVg, length, width, Vsd, e, n, save_fig):
    gate = np.linspace(0.5, -2, np.size(normIVg[:,1]))
    plt.figure()
    for i in range(0,np.size(Vsd)):
        if Vsd[i]!=0:
            sigma = (length*normIVg[:,i])/(width*Vsd[i])
            mobility = sigma/(e*n)     
            plt.plot(gate,mobility)
        plt.xlabel('V$_{g}$(V)')
        plt.ylabel('mobility (cm$^2$/Vs)')

    if save_fig:
        plt.savefig(source_dir + 'mobility.png')
        
        
   
    
            


"""""""""""""""Start script"""""""""""""""


IVsd, const_gate = make_array_IVs(source_dir, IVsd, const_gate)


plot_ivsd(bias, IVsd, file, save_figs)


plot_R(bias, IVsd, Rarr, width, length,  save_figs)

        
        

normIVg = plot_IVg(IVg, normIVg, length, width, save_figs)

plot_mobility(normIVg, length, width, Vsd, e, n, save_figs)


#maak txt file aan
meta_file = open(source_dir + 'fig_META.dat', 'w')
#vraag om hash
import os
import subprocess
git_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
#schrijf data in txt
meta_file.write('Titel: ....')
meta_file.write('Githash: ....')
#sluit file
meta_file.close()



