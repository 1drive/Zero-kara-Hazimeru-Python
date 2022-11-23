sanggeum = 0
N = int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    tmp = 0
    if a == b == c:
        tmp = 10000 + a * 1000
    elif a == b:
        tmp = 1000 + a * 100
    elif b == c:
        tmp = 1000 + b * 100
    elif c == a:
        tmp = 1000 + c * 100
    else:
        tmp = max(a, b, c) * 100
    sanggeum = max(sanggeum, tmp)
print(sanggeum)