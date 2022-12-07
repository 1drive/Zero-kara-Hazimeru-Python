import sys
N = int(sys.stdin.readline())
coms = 1
for i in range(N):
    coms += int(sys.stdin.readline()) - 1
print(coms)