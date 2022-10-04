import sys
T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a = a % 10
    if a == 9:
        a, b = a/3, b*2
    elif a == 8:
        a, b = a/4, b*3
    elif a == 4:
        a, b = a/2, b*2
    if a == 1:
        print("1")
    elif a == 2:
        if b % 4 == 1:
            print("2")
        elif b % 4 == 2:
            print("4")
        elif b % 4 == 3:
            print("8")
        elif b % 4 == 0:
            print("6")
    elif a == 3:
        if b % 4 == 1:
            print("3")
        elif b % 4 == 2:
            print("9")
        elif b % 4 == 3:
            print("7")
        elif b % 4 == 0:
            print("1")
    elif a == 5:
        print("5")
    elif a == 6:
        print("6")
    elif a == 7:
        if b % 4 == 1:
            print("7")
        elif b % 4 == 2:
            print("9")
        elif b % 4 == 3:
            print("3")
        elif b % 4 == 0:
            print("1")
    elif a == 0:
        print("10")