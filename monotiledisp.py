import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

f = h5py.File("monotiledispexp.h5", "r")
# dset = f["section"][:, :]
# bounds = f["section_bounds"][:]
#
# fig, ax = plt.subplots()
# im = ax.imshow(dset, extent=bounds, interpolation="none", aspect="auto")
# cb = plt.colorbar(im)
#
# plt.show()
# fig.savefig("largemonotilesection.pdf")
# plt.cla()
# 
dset = f["disp"][:, :]
bounds = f["disp_bounds"][:]
bounds[0:4] = [ b * 0.317255 / (2 * np.pi) for b in bounds[0:4]]

fig, ax = plt.subplots()
im = ax.imshow(dset, extent=(bounds[0], bounds[2], bounds[4], bounds[5]), interpolation="none", aspect="auto", norm=PowerNorm(gamma=0.5))
ax.set_title("Tvísturmynstur eftir $k_x$ ás, $k_y=0$,\n jöfn kúplun milli punkta, kvaðratrótarnorm")
ax.set_xlabel("$k$ [$2\\pi / a$]")
ax.set_ylabel("$E$ (arb. units)")
cb = plt.colorbar(im)
plt.show()
fig.savefig("monotiledispexp.png")
