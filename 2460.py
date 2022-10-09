nowP = 0
ans = 0
for i in range(10):
    A, B = map(int, input().split())
    nowP = nowP + B - A
    ans = max(ans, nowP)
print(ans)