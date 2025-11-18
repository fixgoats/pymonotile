import matplotlib.pyplot as plt
import h5py
import numpy as np

f = h5py.File("kitegriddosexp.h5", "r")
dset = f["energies"][:, :, :]
bounds = f["energies_bounds"][:]

nbins = 400
counts, bins = np.histogram(dset, nbins)
total = sum(counts)
fig, ax = plt.subplots()
ax.stairs(counts / total, bins)
ax.set_title("Ástandsþéttleiki drekagrindar, vísislækkandi kúplun")
ax.set_xlabel("E [arb. units]")
plt.show()
fig.savefig("kitegriddosexp.png")
