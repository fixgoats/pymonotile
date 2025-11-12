<<<<<<< HEAD
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
=======
import h5py
import numpy as np
import matplotlib.pyplot as plt

f = h5py.File("graphenesection.h5", "r")
dset = f["section"][:,:]
bounds = f["section_bounds"][:]
# dset = f["sdf"]
# bounds = f["sdf_bounds"]

# zerokysection = dset[:,0,:]
# bounds = bounds[:]

# fig, ax = plt.subplots()
# im1 = ax.imshow(zerokysection.T, extent=[bounds[0], bounds[1], bounds[4], bounds[5]], origin="lower", interpolation="none", aspect='auto')
# cb = plt.colorbar(im1)
# 
# ax.set_xlabel("$k_x")
# ax.set_ylabel("$E$")
# ax.set_title("Dispersion relation ($k_y = 0$)")
# 
# fig.savefig("disprelation.pdf")
# plt.show()
# plt.cla()
fig, ax = plt.subplots()
# midesection = dset[:,:,99]
im2 = ax.imshow(dset, extent=[bounds[0], bounds[1], bounds[2], bounds[3]], aspect="auto", origin="lower", interpolation="none")
cb = plt.colorbar(im2)

ax.set_xlabel("$k_x$")
ax.set_ylabel("$k_y$")
# de = (bounds[5] - bounds[4]) / 100
# mide = bounds[4] + 99 * de
ax.set_title(f"Spectral density at $E = {bounds[4]}$")
fig.savefig("grapheneesection.pdf")
plt.show()
# plt.cla()
# fig, ax = plt.subplots()
# dos = np.sum(dset[:,:,:], axis=(0, 1))
# es = np.linspace(bounds[4], bounds[5], 200, endpoint=False)
# 
# ax.plot(es, dos)
# ax.set_xlabel("$E$")
# ax.set_ylabel("$\\rho(E)$")
# ax.set_title("Density of states")
# plt.show()
# fig.savefig("densityofstates.pdf")
>>>>>>> 1668691 (exact dispersion for monotile superlattice)
