# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 15:47:28 2015

@author: verajanssen
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import fnmatch


source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[QDs]Hallbar_and_liquid_gate/measurements_square_lattices/Liquid_gate/Sample_6_7_2015_13/'
filename = '155647_[AH]_Vb10mV_Vg1.25V_B0T'

data = np.loadtxt(source_dir + filename + '.dat')

plt.figure()
plt.semilogy(data[:,0], data[:,1])
plt.xlabel('Vg(V)')
plt.ylabel('Isd(nA)')