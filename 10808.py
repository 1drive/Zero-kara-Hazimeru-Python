abcarr = [0 for _ in range(26)]
S = input().strip()
for i in S:
    abcarr[ord(i)-97] += 1
for i in abcarr:
    print(i, end=" ")