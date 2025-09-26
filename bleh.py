import numpy as np
from scipy.linalg import eigvals, expm
import matplotlib.pyplot as plt
from numba import njit

a = 1
N = 20
grid = np.array([
    [a*i, a*j] for i in range(N)
    for j in range(N)
])


# Assumes a is sorted
# @njit
# def delta(a, x):
#     i = 0
#     while True:
#         if a[i] >= x:
#             break
#         i += 1
#     return i

@njit
def adeltab(a, b, n):
    return np.array([[x * y for x in b[n,:]] for y in a[:,n]])


beta = 100
nk = 100
dk = 2 * np.pi / (nk * a)
krange = np.arange(-np.pi / a, np.pi / a, dk)

ham = np.zeros((N*N, N*N))

t = 1
for i in range(N):
    for j in range(i, N):
        if i < N-1:
            ham[i*N+j, i*N + j + 1] = t
            ham[i*N + j + 1, i*N+j] = t
        if j < N-1:
            ham[i*N+j, (i+1)*N + j] = t
            ham[(i+1)*N + j, i*N+j, ] = t

        if j > 0:
            ham[i*N+j, i*N + j - 1] = t
            ham[i*N + j - 1, i*N+j] = t
        if i > 0:
            ham[i*N+j, (i-1)*N + j] = t
            ham[(i-1)*N + j, i*N+j, ] = t



emin = 0
emax = 4
n_es = 100
de = (emax - emin) / n_es
eigvals, eigvecs = np.linalg.eigh(ham)
inv_eigvecs = np.linalg.inv(eigvecs)
diag_ham = np.diag(eigvals)
es = np.arange(emin, emax, de)
fuzz = 50


@njit
def approx_delta(x):
    tmp = np.exp(-fuzz*x**2)
    for x in tmp:
        x = x > 0.9

# es = np.zeros((nk))
# for j, k in enumerate(krange):
#     k_vec = (1/N) * np.array([np.exp(1j * (k * r[0] )) for r in grid])
#     es[j] = np.dot(k_vec.conj(), ham @ k_vec)
# 
# fig, ax = plt.subplots()
# ax.plot(krange, es)
# fig.savefig("disp.pdf")
# plt.show()

density = np.zeros((nk, n_es))
for j, k in enumerate(krange):
    for i, e in enumerate(es):
        delta = eigvecs @ np.diag(approx_delta(eigvals - e)) @ inv_eigvecs
        k_vec = (1/N) * np.array([np.exp(1j * k * r[0]) for r in grid])
        density[j, i] = np.dot(k_vec.conj(), np.matmul(delta, k_vec)).real


fig, ax  = plt.subplots()

ax.imshow(density)
fig.savefig("density.pdf")
plt.show()
