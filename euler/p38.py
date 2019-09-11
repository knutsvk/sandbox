def is_pandigital(s):
    return all([list(s).count(str(i)) for i in range(1, len(s) + 1)])


def concatenated_product(number, largest_integer):
    return "".join([str(number * i) for i in range(1, largest_integer + 1)])

if __name__ == "__main__":
    largest = "918273645"
    number = 1
    while number < 10000:
        largest_integer = 2
        ccp = concatenated_product(number, largest_integer)
        while len(ccp) < 10:
            if is_pandigital(ccp):
                if ccp > largest:
                    largest = ccp
            largest_integer += 1
            ccp = concatenated_product(number, largest_integer)
        number += 1
    print(largest)
