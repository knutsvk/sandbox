if __name__ == "__main__":
    tree = [[int(x) for x in l] for l in [line.split() for line in open("p67.in")]]
    tree.reverse()
    for i in range(1, len(tree)):
        for j in range(len(tree[i])):
            tree[i][j] += max(tree[i-1][j], tree[i-1][j+1])
    print(tree[-1][-1])
