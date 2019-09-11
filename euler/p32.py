from itertools import permutations

if __name__ == "__main__":
    products = set()
    n = 9
    for perm in permutations(range(1, n + 1)):
        perm = list(perm)
        for i in range(1, n-1):
            for j in range(i+1, n):
                a = int("".join([str(x) for x in list(perm)[:i]]))
                b = int("".join([str(x) for x in list(perm)[i:j]]))
                c = int("".join([str(x) for x in list(perm)[j:]]))
                if a * b == c:
                    print("%d * %d = %d" % (a,b,c))
                    products.add(c)
    print(sum(products))
