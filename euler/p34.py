from math import factorial


def digit_factorial_sum(x):
    return sum([factorial(int(y)) for y in str(x)])


def is_curious(x):
    return x == digit_factorial_sum(x)


if __name__ == "__main__":
    print(sum([x for x in range(10,100000) if is_curious(x)]))
