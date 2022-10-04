import sys
n, q = map(int, sys.stdin.readline().split())
tnduf = list(map(int, sys.stdin.readline().split()))
tmpquery = []
for _ in range(q):
    tmpquery = list(map(int, sys.stdin.readline().split()))
    if tmpquery[0] == 1:
        sum = 0
        for _ in range(tmpquery[1] - 1, tmpquery[2]):
            sum += tnduf[_]
        print(sum)
        tmp = tnduf[tmpquery[2] - 1]
        tnduf[tmpquery[2] - 1] = tnduf[tmpquery[1] - 1]
        tnduf[tmpquery[1] - 1] = tmp
    elif tmpquery[0] == 2:
        sumab = 0
        sumcd = 0
        for _ in range(tmpquery[1] - 1, tmpquery[2]):
            sumab += tnduf[_]
        for _ in range(tmpquery[3] - 1, tmpquery[4]):
            sumcd += tnduf[_]
        print(sumab - sumcd)