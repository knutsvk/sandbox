ans = 1
spiral = 1
last = 1
while spiral < 1001:
    spiral += 2
    adder = spiral - 1
    for i in range(4):
        last = last + adder
        ans += last
print(ans)

