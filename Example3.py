# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 13:20:43 2024

@author: mdubo
"""

import matplotlib.pyplot as plt
import numpy as np

TE = np.array([3, 5, 4, 7, 8, 2, 6, 6, 5, 4, 3, 9, 8, 4, 7, 2, 4, 3, 4, 8, 6]); #Numpy array for thermal energy values

plt.hist(TE, bins=7);
plt.xlabel('Thermal Energies (J)')
plt.ylabel('Frequencies')
plt.title("Distribution of Thermal Energies at Different Temperatures")
plt.show()

