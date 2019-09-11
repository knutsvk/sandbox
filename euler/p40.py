from math import ceil 


def limits(nmax):
    i = 0
    ret = [0]
    while ret[-1] < 1000000:
        ret.append(ret[i] + 9 * (i+1) * 10 ** i)
        i += 1
    return ret


if __name__ == "__main__":
    lims = limits(6)
    result = 1
    for e in range(7):
        dig = 10 ** e
        for i,l in enumerate(lims[1:]):
            if dig <= l:
                num = 10 ** i - 1 + ceil((dig - lims[i]) / (i + 1))
                idx = (dig - lims[i] - 1) % (i+1)
                result *= int(str(num)[idx])
                break
    print(result)
                
