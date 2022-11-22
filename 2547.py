T = int(input())
for i in range(T):
    tmp = input()
    s = int(input())
    sumofC = 0
    for j in range(s):
        sumofC += int(input())
    if sumofC % s == 0:
        print("YES")
    else:
        print("NO")