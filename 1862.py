M = int(input())
wkfltn, sum = 0, 0
for _ in range(len(str(M))):
    wkfltn += 1
    target = int(str(M)[::-1][_])
    tmp = 1
    if wkfltn > 1:
        for i in range(wkfltn-2):
            tmp = tmp * 9 + 10 ** (i+1)
        if target > 4:
            tmp = tmp * (target-1) + 10**(wkfltn-1)
        else:
            tmp = tmp * (target)
        sum += tmp
    elif wkfltn == 1:
        if target > 4:
            sum += 1
print(M-sum)