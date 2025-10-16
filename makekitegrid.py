import numpy as np
import matplotlib.pyplot as plt

a = 0.24595
a_cc = 0.142

a1 = np.array([a, 0])
a2 = np.array([a/2, np.sqrt(3) * a/2])

o1 = np.array([0, -a_cc / 2])
o2 = np.array([0, a_cc / 2])
o3 = np.array([0, 0])
o4 = np.array([np.sqrt(3) / 2 * a_cc, 0])
o5 = np.array([np.sqrt(3) / 4 * a_cc, 3 * a_cc / 4])
o6 = np.array([np.sqrt(3) / 4 * a_cc, -3 * a_cc / 4])
grid = np.ndarray((0,2))
for i in range(4):
    for j in range(4):
        p1 = i*a1 + j*a2 + o1
        p2 = i*a1 + j*a2 + o2
        p3 = i*a1 + j*a2 + o3
        p4 = i*a1 + j*a2 + o4
        p5 = i*a1 + j*a2 + o5
        p6 = i*a1 + j*a2 + o6
        grid = np.vstack((grid, [p1], [p2], [p3], [p4], [p5], [p6]))

# midpoint = 35*a1 + 35*a2
# mask = np.linalg.norm(grid - midpoint, axis=1) < 5
# print(mask)
# grid = grid[mask,:]
# print(grid)

np.savetxt("kitegrid.txt", grid)

fig, ax = plt.subplots()
ax.scatter(grid[:, 0], grid[:, 1])
plt.show()
