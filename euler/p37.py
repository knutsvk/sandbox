from p35 import prime_sieve


if __name__ == "__main__":
    primes = prime_sieve(1000000)
    interesting_numbers = []
    for p in primes[4:]:
        strp = str(p)
        interesting = True
        for i in range(1, len(strp)):
            if int(strp[i:]) not in primes or int(strp[:-i]) not in primes:
                interesting = False
                break
        if interesting: 
            interesting_numbers.append(p)
    print(sum(interesting_numbers))
