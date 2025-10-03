import matplotlib.pyplot as plt
import numpy as np

points = np.loadtxt("smallermonotilepoints.txt")
fig, ax = plt.subplots()

points = points[points[:, 0] > 5]
points = points[points[:, 0] < 15]
points = points[points[:, 1] > -1]
points = points[points[:, 1] < 9]

ax.scatter(points[:, 0], points[:, 1])
plt.show()

np.savetxt("filteredpoints.txt", points)
