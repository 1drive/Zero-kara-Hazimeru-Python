import sys
for _ in range(3):
    S = 0
    for i in range(int(sys.stdin.readline())):
        S += int(sys.stdin.readline())
    if S > 0:
        print("+")
    elif S < 0:
        print("-")
    elif S == 0:
        print("0")