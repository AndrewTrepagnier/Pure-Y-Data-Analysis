import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

array_dft = []
array_hpc =[]

"""
   After open(), ev_data is a file object, not an array. It's essentially a handle or connection to the file that allows 
   you to read from it. You can think of it as a stream of text that you can read line by line.

   Didn't use this approach because pandas can handle all file opening/closing automatically and convert strings to numbers

"""

array_dft = pd.read_csv('/Users/andrewtrepagnier/.cursor-tutor/projects/Pure_y/Pure-Y-Data-Analysis/EV_DFT.txt', sep=r'\s+', skiprows=0).values
array_hpc = pd.read_csv('/Users/andrewtrepagnier/.cursor-tutor/projects/Pure_y/Pure-Y-Data-Analysis/Y_hcp.txt', sep=r'\s+', skiprows=0 ).values
dft_volume_column = array_dft[:, 0] #Refresh:  : all rows, 0 slices it so means first column
dft_energy_column = array_dft[:, 1] /2

hpc_volume_column = array_hpc[:, 0] /2
hpc_energy_column = array_hpc[:, 1]



# print(len(volume_column))
# print(volume_column)

# print(len(energy_column))
# print(energy_column)

#plt.scatter(volume_column, energy_column, 'b', 'o')

plt.figure(figsize = (10,8))
plt.plot(dft_volume_column, dft_energy_column, 'r', label='DFT Data')
plt.plot(hpc_volume_column, hpc_energy_column, 'b', label= 'RANN Data')
plt.xlabel('Volume (Å³)')
plt.ylabel('Energy (eV)')
plt.legend()
plt.title('Pure Crystalline Y EV Curve')

plt.savefig('/Users/andrewtrepagnier/.cursor-tutor/projects/Pure_y/Pure-Y-Data-Analysis/DFT_EV_curves.png')
plt.show()




