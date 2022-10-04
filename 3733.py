import sys
import math
while True:
    try:
        N, S = map(int, sys.stdin.readline().split())
        print(math.floor(S / (N+1)))
    except:
        break