import numpy as np
from p21 import sum_proper_divisors


def get_abundant_numbers(limit):
    i = 12
    result = [i]
    while i < limit-12:
        i += 1
        if sum_proper_divisors(i) > i:
            result.append(i)
    return result


if __name__ == "__main__":
    limit = 28123
    abundants = np.array(get_abundant_numbers(limit))
    two_abundants_sums = np.unique(np.add.outer(abundants, abundants))
    two_abundants_sums = [x for x in two_abundants_sums if x <= limit]
    print(limit*(limit+1)//2-sum(two_abundants_sums))
