import sys
N, M, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort(reverse=True)
secondBig = M // (K+1)
print(A[0] * (M - secondBig) + A[1] * secondBig)