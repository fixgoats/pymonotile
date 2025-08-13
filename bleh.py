import numpy as np

vertices = np.loadtxt("smallermonotilepoints.txt")
N = np.shape(vertices)[0]
b = np.zeros((N, N))
for i in range(N):
    for j in range(i):
        d = np.linalg.norm(vertices[i, :])
        if d < 3.9:
            b[i, j] = np.exp(-d)
            b[j, i] = np.exp(-d)

eigvals, eigvec = np.linalg.eigh(b)
np.savetxt("frequencies.txt", eigvals)
np.savetxt("eigvecs.txt", eigvec)
