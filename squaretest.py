from pythtb import tb_model
import matplotlib.pyplot as plt
import numpy as np


def square_grid(n):
    return [[float(j) / n, float(i) / n] for i in range(n) for j in range(n)]


N = 2
lat = [[N, 0], [0, N]]
orb = square_grid(N)

square = tb_model(2, 2, lat, orb)

for i in range(N):
    for j in range(N):
        if j == N - 1:
            square.set_hop(-1, i * N + j, i * N, [1, 0])
        else:
            square.set_hop(-1, i * N + j, i * N + j + 1, [0, 0])

        if i == N - 1:
            square.set_hop(-1, i * N + j, j, [0, 1])
        else:
            square.set_hop(-1, i * N + j, (i + 1) * N + j, [0, 0])

kn = 20
kmesh = square_grid(kn)
k = np.linspace(0, 1, kn, endpoint=False)
kxv, kyv = np.meshgrid(k, k)
evals = np.array(
    [square.solve_one(k_point=kmesh[i * N + j]) for j in range(kn) for i in range(kn)]
)
evals = np.reshape(evals, (kn, kn, N * N))
print(evals)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
for i in range(N * N):
    ax.plot_surface(kxv, kyv, evals[:, :, i])
plt.show()
