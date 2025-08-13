import matplotlib.pyplot as plt
import numpy as np
from qutip import basis

N = 20

kx = np.linspace(0, np.pi, N)

H = sum([-basis(N, i) * basis(N, i + 1).dag() for i in range(N - 1)])
H += sum([-basis(N, i + 1) * basis(N, i).dag() for i in range(N - 1)])

evals, ekets = H.eigenstates()

fig, ax = plt.subplots()

np.savetxt("chainqutip.txt", evals)

fig, ax = plt.subplots()
ax.plot(kx, evals)

fig.savefig("chain.pdf")
