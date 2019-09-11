n = 1000

def test0(n):
    """
    Runtime 9.4  s with n = 50
    """
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                for d in range(1, n+1):
                    if a**3 + b**3 == c**3 + d**3:
                        print(a,b,c,d)

def test1(n):
    """
    Runtime 297 ms with n = 50
    Runtime 2.6 s with n = 100
    """
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):
                num = a**3 + b**3 - c**3
                if num > 0:
                    d = round((num)**(1./3))
                    if a**3 + b**3 == c**3 + d**3 and d <= n:
                        print(a,b,c,d)

def test2(n):
    """
    Runtime 152 ms with n = 50
    Runtime 1.22 s with n = 100
    """
    for a in range(1, n+1):
        for b in range(a, n+1):
            for c in range(1, n+1):
                num = a**3 + b**3 - c**3
                if num > 0:
                    d = round((num)**(1./3))
                    if a**3 + b**3 == c**3 + d**3 and d <= n:
                        print(a, b, c, d)
                        if b > a: 
                            print(b, a, c, d)

def test3(n):
    """
    Runtime 83.4 ms with n = 50
    Runtime 679 ms with n = 100
    Runtime 6.9 s with n = 1000
    """
    for a in range(1, n+1):
        print(a, a, a, a)
        for b in range(a+1, n+1):
            memo = [a, b]
            print(a, b, a, b)
            print(a, b, b, a)
            print(b, a, a, b)
            print(b, a, b, a)
            if max(a, b) + min(a, b) > n + 1:
                possibilities = range(min(a,b), n+1)
            else:
                possibilities = range(1, max(a,b))
            for c in possibilities:
                if c in memo:
                    continue
                num = a**3 + b**3 - c**3
                if num > 0:
                    d = round((num)**(1/3))
                    if a**3 + b**3 == c**3 + d**3 and d <= n:
                        print(a, b, c, d)
                        print(a, b, d, c)
                        print(b, a, c, d)
                        print(b, a, d, c)
                        memo.extend([c, d])

def test4(n):
    """
    Runtime  with n = 50
    Runtime  with n = 100
    Runtime  with n = 1000
    """
    result = []
    memo = {}
    for a in range(1, n+1):
        for b in range(1, n+1):
            cubeSum = a**3 + b**3
            if cubeSum in memo:
                memo[cubeSum].append((a,b))
            else:
                memo[cubeSum] = [(a,b)]

    for key, entries in memo.items(): 
        [result.append((a,b,c,d)) for (a,b) in entries for (c,d) in entries]
    return result


if __name__ == "__main__":
    test4(n)

