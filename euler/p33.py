from math import isclose


if __name__ == "__main__":
    product = 1
    for i in range(1,10):
        for j in range(1,10):
            if i != j:
                for k in range(1,10):
                    a = int(str(i) + str(k))
                    b = int(str(k) + str(j))
                    if isclose(i/j, a/b):
                        product *= a/b
    print(product)
