from pythtb import tb_model
import matplotlib.pyplot as plt

lat = [[8]]
orb = [[0], [2], [3], [5], [7]]

chain = tb_model(1, 1, lat, orb)
chain.set_hop(1, 0, 1, [0])
chain.set_hop(2, 1, 2, [0])
chain.set_hop(1, 2, 3, [0])
chain.set_hop(1, 3, 4, [0])
chain.set_hop(2, 4, 0, [1])

chain.display()

(k_vec, k_dist, k_node) = chain.k_path("full", 100)
k_label = ("$0$", r"$\pi$", r"$2\pi$")

evals = chain.solve_all(k_vec)
simplelat = [[1.0]]
simpleorb = [[0.0]]
my_model = tb_model(1, 1, lat, orb)
my_model.set_hop(1.0, 0, 0, [1])

# define a path in k-space
(simplek_vec, simplek_dist, simplek_node) = my_model.k_path("full", 100)

# solve model
simple_evals = my_model.solve_all(k_vec)


fig, ax = plt.subplots()
ax.plot(k_dist, evals[0])
ax.plot(simplek_dist, simple_evals[0])
ax.set_title("1D chain band structure")
ax.set_xlabel("Path in k-space")
ax.set_ylabel("Band energy")
ax.set_xticks(k_node)
ax.set_xticklabels(k_label)
ax.set_xlim(k_node[0], k_node[-1])
for n in range(len(k_node)):
    ax.axvline(x=k_node[n], linewidth=0.5, color="k")
fig.tight_layout()
fig.savefig("fibonacchichain.pdf")
