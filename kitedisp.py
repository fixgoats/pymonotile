import matplotlib.pyplot as plt
import h5py
import numpy as np

f = h5py.File("kitegriddispexp.h5", "r")
dset = f["disp"][:, :]
bounds = f["disp_bounds"][:]
print(bounds)

dk = (bounds[3] - bounds[1]) / 400
k = np.arange(bounds[1], bounds[3], dk)

fig, ax = plt.subplots()
for i in range(6):
    plt.plot(k, dset[:, i])

ax.set_title("Tvísturmynstur drekagrindar eftir $k_x$, $k_y=0$.\nVísislækkandi kúplanir.")
ax.set_xlabel("$k_x$ [1 / a]")
ax.set_ylabel("E (arb. units)")
plt.show()
fig.savefig("kitedispexp.png")
