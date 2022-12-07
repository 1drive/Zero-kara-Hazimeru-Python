import sys
A, B, C = map(int, sys.stdin.readline().split())
if B - A >= C - B:
    print(B-A-1)
else:
    print(C-B-1)