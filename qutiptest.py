import matplotlib.pyplot as plt
from qutip import basis, expect
import numpy as np

N = 20

kx = np.linspace(0, np.pi, N)

kxv, kyv = np.meshgrid(kx, kx)

h = sum(
    [
        -basis(N * N, j * N + i) * basis(N * N, (j + 1) * N + i).dag()
        for i in range(N)
        for j in range(N - 1)
    ]
)
h += sum(
    [
        -basis(N * N, j * N + i) * basis(N * N, (j - 1) * N + i).dag()
        for i in range(N)
        for j in range(1, N)
    ]
)
h += sum(
    [
        -basis(N * N, j * N + i) * basis(N * N, j * N + i + 1).dag()
        for i in range(N - 1)
        for j in range(N)
    ]
)
h += sum(
    [
        -basis(N * N, j * N + i) * basis(N * N, j * N + i - 1).dag()
        for i in range(1, N)
        for j in range(N)
    ]
)

# evals, ekets = H.eigenstates()
# reordered = np.zeros((N, N))
# idx = 0
# for i in range(N):
#     for j in range(i):
#         for k in range(i - j):
#             reordered[i, j] = evals[idx]
#             idx += 1


dk = np.pi / N
bleh = np.arange(0, np.pi, dk)
r_basis = [basis(N * N, j * N + i) for i in range(N) for j in range(N)]
# k_basis = np.array([[
#     (1 / N)
#     * 
#     )
#     for kx in bleh]
#     for ky in bleh
# ])


es = np.array([
              [
              expect(h, sum(
        [
            np.exp(1j * (kx * i + ky * j)) * basis(N * N, j * N + i)
            for i in range(N)
            for j in range(N)
        ])/ N)  for kx in bleh]
              for ky in bleh]
              )
print(es)

# np.savetxt("squarefreq.txt", evals)
# np.savetxt("squareigvecs.txt", evals)

analytical = -2 * (np.cos(kxv) + np.cos(kyv))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(kxv, kyv, es)
ax.plot_surface(kxv, kyv, analytical)
#
plt.show()
fig.savefig("square.pdf")
