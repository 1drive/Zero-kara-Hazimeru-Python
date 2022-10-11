N = int(input())
res = 0
for i in range(N):
    a, d, g = map(int, input().split())
    if a == d + g:
        score = 2 * a * (d + g)
    else:
        score = a * (d + g)
    res = max(res, score)
print(res)