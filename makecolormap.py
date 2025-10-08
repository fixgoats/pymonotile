import h5py
import numpy as np
import matplotlib.pyplot as plt

f = h5py.File("densities.h5", "r")
dset = f["matrix"]

array = f["matrix"][:, :]
bounds = f["bounds"][:]

fig, ax = plt.subplots()

ax.imshow(array, extent=bounds, origin="lower", interpolation="none")
ax.set_xlabel("$k_x$")
ax.set_ylabel("$E$")
ax.set_title("Dispersion relation")

fig.savefig("densitymap.pdf")

plt.show()
plt.cla()
fig, ax = plt.subplots()
dos = f["dos"][:]
es = np.linspace(bounds[2], bounds[3], 300, endpoint=False)
# counts, bins = np.histogram(es, bins=100)
# ax.stairs(counts, bins)
ax.plot(es, dos / np.sum(dos))
ax.set_xlabel("$E$")
ax.set_ylabel("$\\rho(E)$")
ax.set_title("Density of states")
plt.show()
fig.savefig("dos.pdf")
