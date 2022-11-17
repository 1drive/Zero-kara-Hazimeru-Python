N = int(input())
for i in range(N):
    a, b, c, d = map(int, input().split())
    if a * b > c * d:
        print("TelecomParisTech")
    elif a * b < c * d:
        print("Eurecom")
    elif a * b == c * d:
        print("Tie")