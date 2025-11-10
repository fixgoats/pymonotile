import matplotlib.pyplot as plt
import h5py
import numpy as np

f = h5py.File("motherdos.h5", "r")
dset = f["energies"][:, :, :]
bounds = f["energies_bounds"][:]

nbins = 200
counts, bins = np.histogram(dset, nbins)
plt.stairs(counts, bins)
plt.show()
