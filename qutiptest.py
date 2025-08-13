import matplotlib.pyplot as plt
import numpy as np
from qutip import basis

N = 20

kx = np.linspace(0, np.pi, N)

kxv, kyv = np.meshgrid(kx, kx)

H = sum(
    [
        basis(N * N, j * N + i) * basis(N * N, (j + 1) * N + i).dag()
        for i in range(N)
        for j in range(N - 1)
    ]
)
H += sum(
    [
        basis(N * N, j * N + i) * basis(N * N, (j - 1) * N + i).dag()
        for i in range(N)
        for j in range(1, N)
    ]
)
H += sum(
    [
        -basis(N * N, j * N + i) * basis(N * N, j * N + i + 1).dag()
        for i in range(N - 1)
        for j in range(N)
    ]
)
H += sum(
    [
        -basis(N * N, j * N + i) * basis(N * N, j * N + i - 1).dag()
        for i in range(1, N)
        for j in range(N)
    ]
)

evals, ekets = H.eigenstates()
reordered = np.zeros((N, N))
idx = 0
for i in range(N):
    for j in range(i):
        for k in range(i - j):
            reordered[i, j] = evals[idx]
            idx += 1

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

np.savetxt("squarequtip.txt", evals)

ax.plot_surface(kxv, kyv, reordered)

fig.savefig("square.pdf")
