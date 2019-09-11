from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
from ising import heat_bath

# TODO: 
# L and N should be command line arguments
# make faster with numba / cython
# do the rest of the computations to obtain results

sns.set()

L = 30
N = 1000*L**2

lattice1 = -1 + 2 * np.random.randint(0, 2, size=(L,L))
lattice1[:,0] = -1
lattice2 = np.copy(lattice1)
lattice2[:,0] = 1
lattices = [lattice1, lattice2]

fig = plt.figure(num=1, figsize=(5,5))
ax = fig.add_subplot(2,2,1)
sns.heatmap(lattices[0])
ax = fig.add_subplot(2,2,2)
sns.heatmap(lattices[1])

heat_bath(L, N, lattices)

ax = fig.add_subplot(2,2,3)
sns.heatmap(lattices[0])
ax = fig.add_subplot(2,2,4)
sns.heatmap(lattices[1])
fig.show()
