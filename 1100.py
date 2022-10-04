sum = 0
for i in range(8):
    line = input().strip()
    if (i % 2) == 1:
        line = line[1] + line[3] + line[5] + line[7]
    else:
        line = line[0] + line[2] + line[4] + line[6]
    sum += line.count("F")
print(sum)