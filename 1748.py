N = int(input())
sum = 0
i = 1
while i <= N:
    sum += (N-i+1)
    i *= 10
print(sum)