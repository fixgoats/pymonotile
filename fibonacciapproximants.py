from pythtb import tb_model
import matplotlib.pyplot as plt
from functools import cache
import numba as nb
from numba.typed import List


@cache
def fibwordgen(n):
    if n == 0:
        return [2]
    if n == 1:
        return [2, 1]
    return fibwordgen(n - 1) + fibwordgen(n - 2)


@nb.njit(nb.types.ListType(nb.float64)(nb.types.ListType(nb.int64)))
def word_to_loc(l):
    retl = List([0.0] * len(l))
    s = 0.0
    S = sum(l)
    for i, e in enumerate(l[0:-1]):
        s += e / S
        retl[i + 1] = s
    return retl


@nb.njit
def wrapnums(l):
    return [[e] for e in l]


ninthgen = fibwordgen(8)
typed_ninthgen = List(ninthgen)
print(nb.typeof(typed_ninthgen))
locations = word_to_loc(typed_ninthgen)

lat = [[sum(ninthgen)]]
orb = wrapnums(word_to_loc(typed_ninthgen))

chain = tb_model(1, 1, lat, orb)
for i, e in enumerate(ninthgen):
    t = 1 if e == 2 else 2
    if i == len(ninthgen) - 1:
        chain.set_hop(t, i, 0, [1])
    else:
        chain.set_hop(t, i, i + 1, [0])

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
