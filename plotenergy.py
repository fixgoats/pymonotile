import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

E = np.loadtxt("squarefreq.txt")

k = np.linspace(-np.pi, np.pi, len(E))

ax.plot(k, E)

fig.savefig("squareplot.pdf")
