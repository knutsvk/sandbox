def larger(pair1, pair2):
    return pair1[0] ** (pair1[1] / pair2[1]) / pair2[0] > 1 

if __name__ == "__main__":
    pairs = [line.strip().split(',') for line in open("p99.in")]
    pairs = [[int(x) for x in pair] for pair in pairs]
    largest = 0
    for i, pair in enumerate(pairs):
        if larger(pair, pairs[largest]):
            largest = i
    print(largest+1)


