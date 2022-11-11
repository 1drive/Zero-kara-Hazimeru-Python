N = int(input())
for i in range(N):
    a, b, c, d = map(int, input().split())
    if b >= 10.5 and c >= 7.5 and d >= 12 and b + c + d >= 55:
        print(a, b + c + d, "PASS")
    else:
        print(a, b + c + d, "FAIL")