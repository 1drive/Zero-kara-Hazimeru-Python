import sys
i = sys.stdin.readline().strip()
while i != "0":
    accum = 0
    for j in i:
        j = int(j)
        if j == 1:
            accum += 2
        elif j == 0:
            accum += 4
        else:
            accum += 3
    accum += len(i) + 1
    print(accum)
    i = sys.stdin.readline().strip()