import math
N = int(input())
A = math.sqrt(N)
if A <= 2:
    print(4)
elif int(A) == A:
    print(int(4*(A-1)))
elif A >= math.floor(A) + 0.5:
    print(math.floor(A)*4)
else:
    print(4*math.floor(A-1)+2)