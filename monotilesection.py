import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

f = h5py.File("monotilesection-1exp.h5", "r")
dset = f["section"][:, :]
bounds = f["section_bounds"][:]

fig, ax = plt.subplots()

ax.set_xlabel("$k_x$ [$2\\pi / a$]")

ax.set_ylabel("$k_y$ [$2\\pi / a$]")
ax.set_title("Þéttleika þversnið við E=-1")
im = ax.imshow(dset, extent=bounds, interpolation="none", aspect="auto")
cb = plt.colorbar(im)

plt.show()
fig.savefig("monotilesection-1exp.png")
# plt.cla()
# 
# dset = f["disp"][:, :]
# bounds = f["disp_bounds"][:]
# 
# fig, ax = plt.subplots()
# im = ax.imshow(dset, extent=(bounds[0], bounds[2], bounds[4], bounds[5]), interpolation="none", aspect="auto", norm=PowerNorm(gamma=0.5))
# ax.set_title("Tvísturmynstur eftir skálínu,\n jöfn kúplun milli punkta, kvaðratrótarnorm")
# ax.set_xlabel("$k$ (arb. units)")
# ax.set_ylabel("$E$ (arb. units)")
# cb = plt.colorbar(im)
# plt.show()
# fig.savefig("monotilediagdisp.pdf")
