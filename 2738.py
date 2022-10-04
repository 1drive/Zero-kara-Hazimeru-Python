import sys
N, M = map(int, sys.stdin.readline().split())
Arr1 = []
Arr2 = []
for i in range(N):
    Arr1.append(list(map(int, sys.stdin.readline().split())))
for j in range(N):
    Arr2.append(list(map(int, sys.stdin.readline().split())))
oneLineMsg = []
for k in range(N):
    for l in range(M):
        oneLineMsg.append(Arr1[k][l] + Arr2[k][l])
    oneLineMsg = list(map(str, oneLineMsg))
    print(" ".join(oneLineMsg))
    oneLineMsg = []