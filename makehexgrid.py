import numpy as np

a = 0.24595
a_cc = 0.142

a1 = np.array([a, 0])
a2 = np.array([a/2, np.sqrt(3) * a/2])

o1 = np.array([0, -a_cc / 2])
o2 = np.array([0, a_cc / 2])
grid = np.ndarray((0,2))
for i in range(100):
    for j in range(100):
        p1 = i*a1 + j*a2 + o1
        p2 = i*a1 + j*a2 + o2
        grid = np.vstack((grid, [p1], [p2]))

midpoint = 35*a1 + 35*a2
mask = np.linalg.norm(grid - midpoint, axis=1) < 5
print(mask)
grid = grid[mask,:]
print(grid)

np.savetxt("largercirchexgrid.txt", grid)
