import h5py
import numpy as np
import matplotlib.pyplot as plt

f = h5py.File("densities.h5", "r")
dset = f["matrix"]

array = f["matrix"][:, :]
bounds = f["bounds"][:]

fig, ax = plt.subplots()

ax.imshow(array, extent=bounds, origin="lower", interpolation="none")

fig.savefig("densitymap.pdf")

plt.show()
plt.cla()
fig, ax = plt.subplots()
dos = f["dos"][:]
es = np.linspace(bounds[2], bounds[3], 100, endpoint=False)
# counts, bins = np.histogram(es, bins=100)
# ax.stairs(counts, bins)
ax.plot(es, dos)
plt.show()
fig.savefig("dos.pdf")
