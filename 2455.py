pas, maxpas = 0, 0
for i in range(4):
    a, b = map(int, input().split())
    pas = pas - a + b
    maxpas = max(maxpas, pas)
print(maxpas)