import matplotlib.pyplot as plt
import numpy as np

# Set global style settings for fonts and gridlines
plt.rcParams.update({
    'font.size': 12,          # Set font size
    'font.family': 'serif',   # Use serif font
    'grid.color': 'gray',     # Gridline color
    'grid.linestyle': '--',   # Gridline style
    'grid.linewidth': 0.5     # Gridline width
})


x = np.array([0, 10, 20, 30, 40])
c_axis_rann = [4.6, 4.65, 4.67, 4.68, 4.69]
c_axis_meam = [4.7, 4.68, 4.67, 4.66, 4.65]
c_axis_kornilov = [4.72, 4.70, 4.69, 4.68, 4.67]
c_axis_rostoker = [4.74, 4.72, 4.71, 4.70, 4.69]

a_axis_rann = [2.85, 2.86, 2.87, 2.88, 2.89]
a_axis_meam = [2.88, 2.87, 2.86, 2.85, 2.84]
a_axis_kornilov = [2.90, 2.89, 2.88, 2.87, 2.86]
a_axis_rostoker = [2.92, 2.91, 2.90, 2.89, 2.88]


fig, ax = plt.subplots(figsize=(8, 6))


ax.plot(x, c_axis_rann, 'o-r', label="RANN")
ax.plot(x, c_axis_meam, '*-g', label="MEAM")
ax.plot(x, c_axis_kornilov, '^--c', label="Kornilov")
ax.plot(x, c_axis_rostoker, 'v-.b', label="Rostoker")

ax.plot(x, a_axis_rann, 'o-r')
ax.plot(x, a_axis_meam, '*-g')
ax.plot(x, a_axis_kornilov, '^--c')
ax.plot(x, a_axis_rostoker, 'v-.b')


ax.grid(True, which='both')


ax.set_xlabel("at.% ...", fontsize=14)
ax.set_ylabel("Lattice Constant (Å)", fontsize=14)
ax.set_xticks(x)
ax.set_yticks(np.arange(2.8, 4.9, 0.2))


ax.legend(loc="upper right", fontsize=12, frameon=False)


plt.tight_layout()


plt.show()
