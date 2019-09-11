import numpy as np


def eratosthenes(n):
    A = np.ones(n, dtype=bool)
    A[0:2] = False
    for i in range(int(np.sqrt(n+1))):
        if A[i]:
            A[i**2::i] = False
    return np.where(A)[0]


if __name__ == "__main__":
    primes = eratosthenes(int(2e6))
    print(sum(primes))
