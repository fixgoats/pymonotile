import numpy as np
import matplotlib.pyplot as plt
import h5py

# points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# H = np.array([
#     [0, 1, 1, 0],
#     [1, 0, 0, 1],
#     [1, 0, 0, 1],
#     [0, 1, 1, 0]
#     ])
points = np.loadtxt("smallmonotilepoints.txt")
# print(points)
H = np.loadtxt("smallmonotileH.txt")

connections = []

for j in range(np.shape(points)[0]):
    connections.append([])
    for i in range(np.shape(points)[0]):
        if H[j, i] != 0:
            connections[j].append(i) 

print(connections)

fig, ax = plt.subplots()
ax.scatter(points[:,0], points[:,1])

for j in range(len(points)):
    for i in connections[j]:
        ax.plot([points[j][0], points[i][0]], [points[j][1], points[i][1]])
        #ax.quiver(points[j][0], points[j][1], points[i][0] - points[j][0], points[i][1] - points[j][1], angles='xy', scale_units='xy', scale=1)

plt.show()
