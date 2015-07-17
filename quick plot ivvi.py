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

source_dir = 'C:/Users/verajanssen/SURFdrive/Werk/Science/Projects/[2Dmat]Liquid_gate_mos2/Device2/Measurements/Chip2/Dev1/gate_sweep/'

for file in os.listdir(source_dir):
    if fnmatch.fnmatch(file, '*.dat'):
        print file
        IV = np.loadtxt(source_dir + file)
        plt.plot(IV[:,0], IV[:,1])
plt.show()