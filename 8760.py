import math
Z = int(input())
for i in range(Z):
    a, b = map(int, input().split())
    print(math.floor(a*b/2))