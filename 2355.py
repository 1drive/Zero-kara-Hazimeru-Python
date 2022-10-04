A, B = map(int, input().split())
A, B = min(A, B), max(A, B)
print(int((A + B) / 2 * (B-A+1)))