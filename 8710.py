import math
k, w, m = map(int, input().split())
ans = math.ceil((w-k)/m)
if ans <= 0:
    ans = 0
print(ans)