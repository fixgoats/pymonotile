from numba import njit
import numpy as np

N = 40

dk = np.pi / N
k = np.arange(0, np.pi, dk)

kxv, kyv = np.meshgrid(k, k)


@njit
def grid_basis(nx, ny, i, j):
    x = np.zeros((ny, nx))
    x[i, j] = 1
    return x


r_basis = np.array([[grid_basis(N, N, j, i) for i in range(N)] for j in range(N)])

k_basis = np.array(
    [
        [
            np.sum(
                [
                    np.exp(1j * (kx * i + ky * j)) * r_basis[j, i]
                    for kx in k
                    for ky in k
                ],
                axis=0,
            )
            for i in range(N)
        ]
        for j in range(N)
    ]
)

t = -1
H = np.sum(
    [
        t * np.outer(r_basis[j, i], r_basis[j + 1, i])
        for i in range(N)
        for j in range(N - 1)
    ],
    axis=0,
)

H += np.sum(
    [
        t * np.outer(r_basis[j, i], r_basis[j - 1, i])
        for i in range(N)
        for j in range(1, N)
    ],
    axis=0,
)

H += np.sum(
    [
        t * np.outer(r_basis[j, i], r_basis[j, i + 1])
        for i in range(N - 1)
        for j in range(N)
    ],
    axis=0,
)

H += np.sum(
    [
        t * np.outer(r_basis[j, i], r_basis[j, i - 1])
        for i in range(1, N)
        for j in range(N)
    ],
    axis=0,
)
