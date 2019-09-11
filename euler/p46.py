import math
import numpy as np
from p35 import prime_sieve


def odd_composite_sieve(n):
    mask = np.ones(n, dtype=bool)
    mask[:2] = False
    for i in range(int(math.sqrt(n)+1)):
        if mask[i]:
            mask[2*i::i] = False
    mask[:2] = True
    composites = np.arange(n)[~mask]
    return composites[composites % 2 != 0]


if __name__ == "__main__":
    primes = prime_sieve(1000)
    odd_composites = odd_composite_sieve(1000)
    print(primes)
    print(odd_composites)
