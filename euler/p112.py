def isbouncy(x):
    strx = str(x)
    increasing = "".join(sorted(strx))
    return True if strx not in [increasing, increasing[::-1]] else False
        

if __name__ == "__main__": 
    limit = 0.99
    bouncies = 0
    i = 100
    while bouncies / i < limit:
        i += 1
        if isbouncy(i):
            bouncies += 1
    print(i)
