C1 = int(input())
n = 1
while C1 != 1:
    if C1 % 2 == 0:
        C1 = int(C1/2)
    elif C1 % 2 == 1:
        C1 = 3 * C1 + 1
    n += 1
print(n)