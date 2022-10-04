import sys
N = int(sys.stdin.readline())
NN = list(range(-100, 101, 1))
for _ in range(len(NN)):
    NN[_] = 0
NNN = list(map(int, sys.stdin.readline().split()))
for _ in range(N):
    NN[NNN[_] + 100] += 1
print(NN[int(input())+100])
    