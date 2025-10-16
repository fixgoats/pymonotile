import numpy as np
import h5py
import matplotlib.pyplot as plt

f = h5py.File("esectioncircgraph.h5", "r")
dset = f["section"][:, :]
bounds = f["section_bounds"][:]
print(bounds)

fig, ax = plt.subplots()
im = ax.imshow(dset, extent=bounds, interpolation="none", aspect="auto")
cb = plt.colorbar(im)

plt.show()
fig.savefig("graphenesectioncirc.pdf")
