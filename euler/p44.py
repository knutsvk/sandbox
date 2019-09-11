def pentagonal(n):
    return n * (3 * n - 1) // 2


def pentafactory(max_value):
    ret = [1]
    while ret[-1] < max_value: 
        ret.append(pentagonal(len(ret)+1))
    return ret


if __name__ == "__main__":
    # silly
    max_value = 10000000
    pentas = pentafactory(max_value)
    smallest_diff = 999999999999
    k = 1
    while k < len(pentas):
        for j in range(k):
            summ = pentas[k] + pentas[j]
            diff = pentas[k] - pentas[j]
            if summ in pentas:
                if diff in pentas:
                    if diff < smallest_diff:
                        smallest_diff = diff
        k += 1
    print(smallest_diff)

    
