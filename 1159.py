N = int(input())
A = []
for i in range(N):
    A.append(input()[0])
sum, fin = 0, ""
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
    if A.count(i) >= 5:
        sum += 1
        fin += i
if sum > 0:
    print(fin)
else:
    print("PREDAJA")