# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:46:05 2024

@author: mdubo
"""

import numpy as np
import matplotlib.pyplot as plt

masses = np.array([1, 4, 10, 17, 33]); #In kg
velocity = 14; #Velocities of the masses in m/s

K = np.zeros(masses.size); #Creates a blank array to later input the kinetic energies of each mass in Joules

for i in range(int(masses.size)):
    K[i] = (1/2)*masses[i]*velocity**2; #Computes each masses kinetic energy

plt.figure(figsize=(7, 5))
plt.bar(masses, K);
plt.xlabel("Mass of Object (kg)");
plt.ylabel(f"Kinetic Energy of Object with Given Velocity {velocity} m/s (J)");
plt.title("Bar Chart of the Kinetic Energies of different Objects with Given Velocity");
plt.tight_layout();
plt.show();
