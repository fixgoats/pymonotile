from pythtb import tb_model
import matplotlib.pyplot as plt
from functools import cache
from numba import njit, typed


@cache
def fibwordgen(n):
    if n == 0:
        return [2]
    if n == 1:
        return [2, 1]
    return fibwordgen(n - 1) + fibwordgen(n - 2)


@njit
def cumsum(l):
    s = None
    retl = [0] * len(l)
    for i, e in enumerate(l):
        if i == 0:
            s = e
            retl[0] = e
        else:
            s += e
            retl[i] = s
    return retl


@njit
def wrapnums(l):
    return [[e] for e in l]


ninthgen = fibwordgen(14)
typed_ninthgen = typed.List(ninthgen)
print(cumsum(typed_ninthgen))

lat = [[sum(ninthgen)]]
orb = wrapnums(cumsum(typed_ninthgen))

chain = tb_model(1, 1, lat, orb)
for i, e in enumerate(ninthgen):
    t = 1 if e == 2 else 2
    if i == len(ninthgen) - 1:
        chain.set_hop(t, i, 0, [1])
    else:
        chain.set_hop(t, i, i + 1, [0])

chain.display()

(k_vec, k_dist, k_node) = chain.k_path("full", 100)
k_label = ("$0$", r"$\pi$", r"$2\pi$")

evals = chain.solve_all(k_vec)

fig, ax = plt.subplots()
fig.set_size_inches(6, 20)
print(len(evals))
for e in evals:
    ax.plot(k_dist, e)
ax.set_title("1D chain band structure")
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy")
ax.set_xticks(k_node)
ax.set_xticklabels(k_label)
ax.set_xlim(k_node[0], k_node[-1])
for n in range(len(k_node)):
    ax.axvline(x=k_node[n], linewidth=0.5, color="k")
fig.tight_layout()
fig.savefig("fibonaccichain.pdf")
