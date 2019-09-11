def generate_increasing(limit):
    increasing = [[1]*9]
    i = 0
    while len(increasing) < limit:
        i += 1
        new_level = [sum(increasing[i-1][j:]) for j in range(9)]
        increasing.append(new_level)
    return increasing

def generate_decreasing(limit):
    decreasing = [[1]*9]
    i = 0
    while len(decreasing) < limit:
        i += 1
        new_level = [sum(decreasing[i-1][:j+1])+1 for j in range(9)]
        decreasing.append(new_level)
    return decreasing

if __name__ == "__main__":
    limit = 1000000
    increasing = sum([sum(level) for level in generate_increasing(limit)])
    decreasing = sum([sum(level) for level in generate_decreasing(limit)])
    print(increasing + decreasing - 9 * limit)
