N, M = map(int, input().split())
d, dbj = [], []
for i in range(N+M):
    d.append(input())
d.sort()
k = 0
while k < N + M - 1:
    if d[k] == d[k+1]:
        dbj.append(d[k])
        k += 2
    else:
        k += 1
print(len(dbj))
for deudbojab in dbj:
    print(deudbojab)