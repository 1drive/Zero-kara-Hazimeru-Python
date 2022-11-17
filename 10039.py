sumOfScore = 0
for i in range(5):
    N = int(input())
    if N <= 40:
        N = 40
    sumOfScore += N
print(sumOfScore//5)