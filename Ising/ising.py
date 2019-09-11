from math import exp
import numpy as np

np.random.seed()

temp_min = 0.5
temp_range = 2

def get_neighbours(i, j, L):
    if i == 0:
        if j == 0:
            return [[L-1, 0, 1], [0, 1, 0]]
        elif j == L-1:
            return [[L-1, 1, 0], [L-1, L-1, L-2]]
        else:
            return [[L-1, 0, 1, 0], [j, j+1, j, j-1]]
    elif i == L-1:
        if j == 0:
            return [[L-2, L-1, 0], [0, 1, 0]]
        elif j == L-1:
            return [[L-2, 0, L-1], [L-1, L-1, L-2]]
        else:
            return [[L-2, L-1, 0, L-1], [j, j+1, j, j-1]]
    elif j == 0:
        return [[i-1, i, i+1], [0, 1, 0]]
    elif j == L-1:
        return [[i-1, i+1, i], [L-1, L-1, L-2]]
    else:
        return [[i-1, i, i+1, i], [j, j+1, j, j-1]]

def count_positive_neighbours(neighbours):
    n_pos = sum(neighbours > 0)
    return n_pos

def temperature(j, L):
    return temp_min + (j - 1) * temp_range / (L - 1)

def boltzmann_weight(n_pos, temp):
    n_neg = 4 - n_pos
    weight = exp(- n_pos / temp)
    partition_func = weight + exp(- n_neg / temp)
    return weight / partition_func

def heat_bath(L, N, lattices):
    xs = np.random.randint(0, L, N)
    ys = np.random.randint(1, L-1, N)
    rands = np.random.rand(N, 2)

    for (i,j,r) in zip(xs, ys, rands):
        mask = get_neighbours(i, j, L) 
        temp = temperature(j, L)
        for (l,lattice) in enumerate(lattices):
            n_pos = count_positive_neighbours(lattice[mask])
            prob = boltzmann_weight(n_pos, temp)
            if prob > r[l]:
                lattice[i,j] = 1
            else:
                lattice[i,j] = -1
