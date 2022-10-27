import sys
input = sys.stdin.readline
N, M = map(int, input().split())
tiles = []
for i in range(N):
    tmp = input().strip()
    tmptile = []
    for tile in tmp:
        tmptile.append(tile)
    tiles.append(tmptile)
res = 0
for j in range(N):
    for k in range(M-1):
        if tiles[j][k] == tiles[j][k+1] == "-":
            res += 1
for l in range(N-1):
    for m in range(M):
        if tiles[l][m] == tiles[l+1][m] == "|":
            res += 1
print(N*M-res)       