import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

f = h5py.File("largemonotile.h5", "r")
dset = f["section"][:, :]
bounds = f["section_bounds"][:]

fig, ax = plt.subplots()
im = ax.imshow(dset, extent=bounds, interpolation="none", aspect="auto")
cb = plt.colorbar(im)

plt.show()
fig.savefig("largemonotilesection.pdf")
plt.cla()

dset = f["disp"][:, :]
bounds = f["disp_bounds"][:]

fig, ax = plt.subplots()
im = ax.imshow(dset, extent=(bounds[0], bounds[2], bounds[4], bounds[5]), interpolation="none", aspect="auto", norm=LogNorm(vmin=np.min(dset)+1e-14, vmax=np.max(dset)))
cb = plt.colorbar(im)
plt.show()
fig.savefig("largemonotiledisp.pdf")
