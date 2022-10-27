N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
res = []

def fold(x, y, N):
    col = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if col != paper[i][j]:
                fold(x, y, N//2)
                fold(x, y+N//2, N//2)
                fold(x+N//2, y, N//2)
                fold(x+N//2, y+N//2, N//2)
                return
    if col == 0:
        res.append(0)
    elif col == 1:
        res.append(1)

fold(0, 0, N)
print(res.count(0))
print(res.count(1))