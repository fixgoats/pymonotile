import h5py
import numpy as np
import matplotlib.pyplot as plt
import os

coords = np.loadtxt("mediumsquarepoints.txt")
#coords = np.loadtxt("mediumsquarepoints.txt")

values = h5py.File("longersquaretetm.h5")

basedir = "longersquarerun"
os.mkdir(basedir)

psip = values["psi"][-1, 0, :]
psim = values["psi"][-1, 1, :]
times = values["time"][:]
s = np.abs(psip)
s /= np.max(s)
s *= 40
fig, ax = plt.subplots()
fig.set_dpi(200)
fig.set_size_inches(14,12)
bleh = ax.scatter(coords[:,0], coords[:,1], c=np.angle(psip), s=s, cmap="twilight")
fig.colorbar(bleh)
fig.savefig(os.path.join(basedir, "scattermappsip.pdf"))
plt.cla()

s12 = psip.conj() * psim
fig, ax = plt.subplots()
bleh = ax.scatter(coords[:,0], coords[:,1], c=2*s12.real, s=s)
fig.colorbar(bleh)
fig.savefig(os.path.join(basedir, "sx.pdf"))
plt.cla()

fig, ax = plt.subplots()
bleh = ax.scatter(coords[:,0], coords[:,1], c=2*s12.imag, s=s)
fig.colorbar(bleh)
fig.savefig(os.path.join(basedir, "sy.pdf"))
plt.cla()

fig, ax = plt.subplots()
bleh = ax.scatter(coords[:,0], coords[:,1], c=(psip*psip.conj() - psim*psim.conj()).real, s=s)
fig.colorbar(bleh)
fig.savefig(os.path.join(basedir, "sz.pdf"))
plt.cla()

psip = values["psi"][:, 0, :]
ref = psip[:,1276]

phasediffs = psip.T * ref.conj()
dphasediffs = np.diff(phasediffs, axis=1) / np.diff(times)
ax.plot(times[0:-1], dphasediffs[::100, :].T.imag, color="black")
fig.savefig(os.path.join(basedir, "phasediffderivative.pdf"))
plt.cla()
fig, ax = plt.subplots()
bleh = ax.plot(times, (psip.conj()*psip).real, color="black")
fig.savefig(os.path.join(basedir, "magnitude.pdf"))
