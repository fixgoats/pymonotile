import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# N = 10
# omega = np.linspace(1, -1, N)
# K = 2.01
# 
# def f(_, y):
#     thj, thi = np.meshgrid(y, y)
#     sinij = np.sum(np.sin(thj - thi), axis=1)
#     print(sinij)
#     return omega + K / (len(sinij)) * sinij
# 
# y0 = np.linspace(-1, 1, N)
# 
# sol = solve_ivp(f, (0, 1), y0, max_step=0.1, min_step=0.1)

y = np.loadtxt("kuramoto.txt")
t = np.arange(np.shape(y[::10,:])[0])

fig, ax = plt.subplots()
for i in range(0, np.shape(y)[1], 2):
    ax.plot(t, y[::10,i] % (2 * np.pi), color="black")
plt.show()
