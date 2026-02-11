from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def f(t, y):
    return [
        y[1],
        np.sin(t) - 4 * y[0]
    ]

sol = solve_ivp(f, (0, 20), [0, 0], max_step=0.01)

u = np.sin(sol.t)

fig, ax = plt.subplots()
ax.plot(u, sol.y[0,:])
plt.show()
