import numpy as np
import h5py
import matplotlib.pyplot as plt

f = h5py.File("esectiongraph.h5", "r")
dset = f["section"][:, :]
bounds = f["section_bounds"][:]
print(bounds)

fig, ax = plt.subplots()
im = ax.imshow(dset, extent=bounds, interpolation="none", aspect="auto")
cb = plt.colorbar(im)

plt.show()
fig.savefig("graphenesection.pdf")
plt.cla()

dset = f["disp"][:, :]
bounds = f["disp_bounds"][:]
print(bounds)

fig, ax = plt.subplots()
im = ax.imshow(dset, extent=(bounds[0], bounds[2], bounds[4], bounds[5]), interpolation="none", aspect="auto")
cb = plt.colorbar(im)
plt.show()
fig.savefig("graphenedisp.pdf")
