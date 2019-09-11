from itertools import permutations
from p35 import prime_sieve


def tup_to_int(tup):
    return int("".join([str(x) for x in tup]))


if __name__ == "__main__":
    perms = permutations(range(0, 10))
    primes = (2, 3, 5, 7, 11, 13, 17)
    ans = 0
    for perm in perms: 
        interesting = True
        for i in range(7):
            if tup_to_int(perm[i+1:i+4]) % primes[i] != 0:
                interesting = False
                break
        if interesting: 
            ans += tup_to_int(perm)
    print(ans)
