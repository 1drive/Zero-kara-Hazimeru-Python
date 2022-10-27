arr = []
for i in range(9):
    arr.append(list(map(int, input().split())))
X, Y, Max = 0, 0, -100
for j in range(9):
    for k in range(9):
        if arr[j][k] > Max:
            Max = arr[j][k]
            X, Y = j+1, k+1
print(Max)
print(X, Y)