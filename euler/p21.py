def sum_proper_divisors(n):
    ans = 1
    for x in range(2,n):
        if n % x == 0:
            ans += x
    return ans


def is_amicable(a):
    b = sum_proper_divisors(a)
    return sum_proper_divisors(b) == a and a != b


if __name__ == "__main__":
    amicable_sum = 0
    for n in range(2,10000):
        if is_amicable(n):
            amicable_sum += n
    print(amicable_sum)
