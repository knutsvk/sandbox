def triangle(n):
    return n * (n + 1) // 2


def pentagonal(n):
    return n * (3 * n - 1) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def numberfactory(formula, max_value):
    ret = [1]
    while ret[-1] < max_value: 
        ret.append(formula(len(ret)+1))
    return ret


if __name__ == "__main__":
    max_value = 10000000000
    tris = numberfactory(triangle, max_value)
    pentas = numberfactory(pentagonal, max_value)
    hexas = numberfactory(hexagonal, max_value)
    for t in tris[1:]: 
        if t in pentas and t in hexas: 
            print(t)
    
