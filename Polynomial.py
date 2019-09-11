
if __name__ == "__main__":
    p1 = {1: -0.3, 2: 4, 3: 0.5}
    p2 = {1: 0.3, 0: -2, 3: 0.5}
    p = p1.copy()
    for power, coef in p2.items(): 
        if power in p:
            if p[power] + coef == 0:
                p.pop(power)
            else:
                p[power] += coef
        else:
            p[power] = coef
    print(p1)
    print(p2)
    print(p)
