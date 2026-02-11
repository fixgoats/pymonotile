import numpy as np
import matplotlib.pyplot as plt

a = 0.24595
a_cc = 0.142

a1 = np.array([a, 0])
a2 = np.array([a/2, np.sqrt(3) * a/2])

o1 = np.array([0, -a_cc / 2])
o2 = np.array([0, a_cc / 2])
grid = np.ndarray((0,2))
<<<<<<< HEAD
n = 20
for i in range(n):
    for j in range(n):
=======
for i in range(71):
    for j in range(71):
>>>>>>> 1668691 (exact dispersion for monotile superlattice)
        p1 = i*a1 + j*a2 + o1
        p2 = i*a1 + j*a2 + o2
        grid = np.vstack((grid, [p1], [p2]))

<<<<<<< HEAD
midpoint = n/2*a1 + n/2*a2
mask = np.linalg.norm(grid - midpoint, axis=1) < n*a/4
print(mask)
grid = grid[mask,:]
print(grid)

fig, ax = plt.subplots()
ax.scatter(grid[:, 0], grid[:, 1])
plt.show()

np.savetxt("smallcirchexgrid.txt", grid)
=======
np.savetxt("largerhexgrid.txt", grid)
>>>>>>> 1668691 (exact dispersion for monotile superlattice)
