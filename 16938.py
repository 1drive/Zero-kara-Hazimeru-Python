import sys
from itertools import combinations
input = sys.stdin.readline
N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
for i in range(1, N+1):
    tmp = list(combinations(A, i))
    for _ in tmp:
        if L <= sum(_) <= R:
            if max(_) - min(_) >= X:
                ans += 1
print(ans)