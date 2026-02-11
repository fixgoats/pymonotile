import pybinding as pb
import math as m
from pybinding.repository import graphene
import matplotlib.pyplot as plt
import numpy as np

model = pb.Model(graphene.monolayer(), pb.translational_symmetry())

# solver = pb.solver.lapack(model)
kpm = pb.kpm(model)
dos = kpm.calc_dos(energy=np.linspace(-3, 3, 200), broadening=0.06, num_random=16)
dos.plot()
plt.show()
