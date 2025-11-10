import pybinding as pb
import math as m
import matplotlib.pyplot as plt
import numpy as np

sqrt3 = m.sqrt(3)
lattice = pb.Lattice(a1=[3, -sqrt3], a2=[3, sqrt3])

lattice.add_sublattices(('A', [0, 0]),
                        ('B', [0, sqrt3]),
                        ('C', [-1, sqrt3]),
                        ('D', [-1.5, sqrt3 / 2]),
                        ('E', [-2, 0]),
                        ('F', [-1.5, -sqrt3 / 2]))

t1 = -1
t2 = -0.8
lattice.add_hoppings(
    ([0, 0], 'A', 'B', t2),
    ([0, 0], 'A', 'D', t2),
    ([0, 0], 'A', 'F', t2),
    ([1, 0], 'A', 'D', t2),
    ([0, 1], 'A', 'F', t2),
    ([1, -1], 'A', 'B', t2),
    ([0, 0], 'B', 'C', t1),
    ([0, 1], 'B', 'E', t1),
    ([0, 0], 'C', 'D', t1),
    ([-1, 1], 'C', 'F', t1),
    ([0, 0], 'D', 'E', t1),
    ([0, 0], 'E', 'F', t1),
)
# To demonstrate this is the right model
# def rectangle(width, height):
#     x0 = width / 2
#     y0 = height / 2
#     return pb.Polygon([[x0, y0], [x0, -y0], [-x0, -y0], [-x0, y0]])
# 
# 
# model = pb.Model(
#     lattice,
#     rectangle(width=3*m.sqrt(12), height=3*m.sqrt(12))
# )
# model.plot()
# plt.show()

# model = pb.Model(lattice, pb.translational_symmetry())
# 
# solver = pb.solver.lapack(model)
# dos = solver.calc_dos(energies=np.linspace(-4, 4, 200), broadening=1)
# dos.plot()
lattice.plot_brillouin_zone(decorate=True)
plt.show()
