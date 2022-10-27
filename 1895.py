R, C = map(int, input().split())
OriginalPixels = []
for i in range(R):
    tmpStr = list(map(int, input().split()))
    tmpPixels = []
    for _ in tmpStr:
        tmpPixels.append(int(_))
    OriginalPixels.append(tmpPixels)
kList, filteredPixels = [], []
for j in range(R-2):
    for k in range(C-2):
        tmpList = [OriginalPixels[j][k], OriginalPixels[j][k+1], OriginalPixels[j][k+2], OriginalPixels[j+1][k], OriginalPixels[j+1][k+1], OriginalPixels[j+1][k+2], OriginalPixels[j+2][k], OriginalPixels[j+2][k+1], OriginalPixels[j+2][k+2]]
        tmpList.sort()
        kList.append(tmpList[4])
    filteredPixels.append(kList)
    kList = []
T = int(input())
sum, b = 0, 0
while b < len(filteredPixels):
    for pixel in filteredPixels[b]:
        if pixel >= T:
            sum += 1
    b += 1
print(sum)