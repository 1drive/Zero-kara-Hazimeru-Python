import math
i = float(input())
while i != 0:
    ans = 1 + i + i ** 2 + i ** 3 + i ** 4
    print(f"{ans:.2f}")
    i = float(input())