"""
a + b + c = p
a^2 + b^2     = c^2
"""


if __name__ == "__main__":
    winner = (120, 3)
    for p in range(1,1000):
        solutions = set()
        smallest_other = p
        for a in range(1,p):
            if a >= smallest_other:
                break
            b = p * (p - 2 * a) / (2 * (p - a))
            bi = p * (p - 2 * a) // (2 * (p - a))
            c = p-a-bi
            if b > 0 and round(b**2) == bi**2 and c > 0:
                smallest_other = min(b, c)
                solutions.add((a,bi,c))
        if len(solutions) > winner[1]:
            winner = (p, len(solutions))
    print(winner[0])
