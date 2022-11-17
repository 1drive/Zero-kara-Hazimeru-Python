T = int(input())
for _ in range(T):
    A, B = map(str, input().split())
    if A == B:
        print("OK")
    else:
        print("ERROR")