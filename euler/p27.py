import numpy as np


def prime_sieve(n):
    A = np.ones(n, dtype=bool)
    A[:2] = False
    for x in range(2, int(np.sqrt(n)+1)):
        if A[x]:
            A[x**2::x] = False
    return np.arange(n)[A]


def quad(a,b,n):
    return n ** 2 + a * n + b


if __name__ == "__main__":
    limit = 1000
    primes = prime_sieve(1000000)
    best_pair = (2, 2)
    largest = 1
    for b in primes[primes <= limit]:
        for a in range(-limit+1, limit):
            n = 0
            while quad(a,b,n) in primes:
                n += 1
            if n > largest:
                best_pair = (a,b)
                largest = n
    print(best_pair[0] * best_pair[1])
