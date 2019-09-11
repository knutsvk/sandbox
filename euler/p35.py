import math
import numpy as np


def cyclic_permutations(x):
    strx = str(x)
    return [int(strx[i:] + strx[:i]) for i in range(len(strx))]


def prime_sieve(n):
    mask = np.ones(n, dtype=bool)
    mask[:2] = False
    for i in range(int(math.sqrt(n)+1)):
        if mask[i]:
            mask[2*i::i] = False
    return np.arange(n)[mask]


if __name__ == "__main__":
    primes = prime_sieve(100000)
    circular = [p for p in primes if all(perm in primes for perm in cyclic_permutations(p))]
    print(len(circular))
