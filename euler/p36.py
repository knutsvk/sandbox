from math import log


def dec2bin(x):
    largest = int(log(x) / log(2)) + 1
    result = [0] * largest

    result[-largest] = 1
    x -= 2 ** (largest - 1)
    while x > 0:
        largest = int(log(x) / log(2)) + 1
        result[-largest] = 1
        x -= 2 ** (largest - 1)

    return "".join([str(d) for d in result])


def is_palindromic(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True


if __name__ == "__main__":
    assert dec2bin(585) == "1001001001"
    assert is_palindromic("585")
    assert is_palindromic("1001001001")
    assert not is_palindromic("5845")
    result = 0
    print("Decimal  Binary")
    for i in range(1, 1000000):
        if is_palindromic(str(i)) and is_palindromic(dec2bin(i)):
            print(i, "\t", dec2bin(i))
            result += i
    print("\nSUM")
    print(result, "\t(", dec2bin(result), ")")
