# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:40:26 2024

@author: mdubo
"""

import numpy as np
import matplotlib.pyplot as plt
import math

v0 = 40; #Initial Velocity (m/s)
theta = 30; #Initial angle in Degrees
g = 9.81; #Gravity constant (m/s^2)

theta = math.radians(theta); #Converts angle to radians

timeintervals = np.linspace(0, 40*2*np.sin(theta)/9.81, 15); #Creates a list of times

x = np.zeros(timeintervals.size); #Creates a blank list of x values
y = np.zeros(timeintervals.size); #Creates a blank list of y values

for i in range(timeintervals.size): #Puts in values to the x and y arrays using the given equations
    x[i] = v0*np.cos(theta)*timeintervals[i];
    y[i] = v0*np.sin(theta)*timeintervals[i] - (1/2)*g*timeintervals[i]**2;

#Sets the size of the plots
plt.subplots(1, 3, figsize=(30,10))

#Plots the graphs
plt.subplot(1,3,1)
plt.plot(timeintervals, x)
plt.xlabel("Time (sec)")
plt.ylabel("Horizontal Distance (m)")
plt.title("Horizontal Distance over Time of a Projectile")

plt.subplot(1,3,2)
plt.plot(timeintervals, y)
plt.xlabel("Time (sec)")
plt.ylabel("Vertical Distance (m)")
plt.title("Vertical Distance over Time of a Projectile")

plt.subplot(1,3, 3)
plt.plot(x, y)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.title("General Motion of a Projectile")
plt.tight_layout()
plt.show()
    
    


