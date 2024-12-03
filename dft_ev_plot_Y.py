import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

array = []

"""
   After open(), ev_data is a file object, not an array. It's essentially a handle or connection to the file that allows 
   you to read from it. You can think of it as a stream of text that you can read line by line.

   Didn't use this approach because pandas can handle all file opening/closing automatically and convert strings to numbers

"""

array = pd.read_csv('/Users/andrewtrepagnier/.cursor-tutor/projects/Pure_y/EV_DFT.txt', sep=r'\s+', skiprows=0).values
volume_column = array[:, 0]
energy_column = array[:, 1]

# print(len(volume_column))
# print(volume_column)

# print(len(energy_column))
# print(energy_column)

plt.figure(figsize = (10,8))
plt.plot(volume_column, energy_column, 'r')
plt.xlabel('Volume (Å³)')
plt.ylabel('Energy (eV)')
plt.legend('DFT Data line')
plt.show()




