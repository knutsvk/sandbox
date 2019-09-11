total = 200
ways = 0
for P2 in range(total, -1, -200):
    for P1 in range(P2, -1, -100):
        for p50 in range(P1, -1, -50):
            for p20 in range(p50, -1, -20):
                for p10 in range(p20, -1, -10):
                    for p5 in range(p10, -1, -5):
                        for p2 in range(p5, -1, -2):
                            ways += 1
print(ways)
