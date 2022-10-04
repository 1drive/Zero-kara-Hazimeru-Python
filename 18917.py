import sys
query = []
s, x = 0, 0
M = int(input())
for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        tmp = query[1]
        s += tmp
        x ^= tmp
    elif query[0] == 2:
        tmp = query[1]
        s -= tmp
        x ^= tmp
    elif query[0] == 3:
        print(s)
    elif query[0] == 4:
        print(x)