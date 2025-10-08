import h5py
import matplotlib.pyplot as plt

f = h5py.File("densities.h5")
dataset = f['aaa']
a = dataset[:,:]
fig, ax = plt.subplots()

im = ax.imshow(a, interpolation="none")
cb = plt.colorbar(im)

fig.savefig("cppdensity.pdf")
plt.show()
