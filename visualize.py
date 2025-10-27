import numpy as np
import matplotlib.pyplot as plt
import h5py

# a = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# H = np.array([
#     [0, 1, 1, 0],
#     [1, 0, 0, 1],
#     [1, 0, 0, 1],
#     [0, 1, 1, 0]
#     ])
points = np.loadtxt("hexgrid.txt")
print(points)
H = np.loadtxt("circgrapheneH.txt")

connections = []

for j in range(np.shape(points)[0]):
    connections.append([np.array([points[j, 0]]), np.array(points[j, 1])])
    for i in range(np.shape(points)[0]):
        if H[j, i] != 0:
            connections[j][0] = np.append(connections[j][0], [points[i,0]]) 
            connections[j][1] = np.append(connections[j][1], [points[i,1]]) 

print(connections)

fig, ax = plt.subplots()
ax.scatter(points[:,0], points[:,1])

for conn in connections:
    ax.plot(conn[0], conn[1])

plt.show()
