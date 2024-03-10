# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:25:20 2024

@author: mdubo
"""

import matplotlib.pyplot as plt

elements = ["Hydrogen", "Helium", "Carbon", "Oxygen", "Other Elements"]; #Creates list of elements
abundances = [75, 23, 0.5, 1, 0.5]; #The abundances of each element in nature

plt.figure(figsize=(10,20))
plt.pie(abundances)
plt.legend(elements)
plt.tight_layout()
plt.show()