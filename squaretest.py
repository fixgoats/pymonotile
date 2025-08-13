import numpy as np

N = 1000
vertices = np.array([[i, j] for i in range(N) for j in range(N)])

couplings = np.zeros((N, N))

for i in range(N):
    for j in range(i):
        d = np.linalg.norm(vertices[i, :])
        if d < 1.1:
            couplings[i, j] = -1
            couplings[j, i] = -1

eigvals, eigvecs = np.linalg.eigh(couplings)
np.savetxt("squarefreq.txt", eigvals)
np.savetxt("squareigvecs.txt", eigvecs)
