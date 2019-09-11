

if __name__ == "__main__":
    names = [line.strip().split(',') for line in open("p22.in")][0]
    names = sorted([name[1:-1] for name in names])
    scores = [sum([ord(char)-64 for char in name]) * (i+1) for i, name in enumerate(names)]
    print(sum(scores))
