N, M = map(int, input().split())
lst = [[] for k in range(N)]
for i in range(N):
    tmp = input()
    for j in tmp:
        lst[i].append(int(j))
area = 1
for k in range(N): #변의 길이
    for l in range(N-k):
        for m in range(M-k):
            if lst[l][m] == lst[l+k][m] == lst[l][m+k] == lst[l+k][m+k]:
                area = max(area, (k+1)*(k+1))
print(area)          
    