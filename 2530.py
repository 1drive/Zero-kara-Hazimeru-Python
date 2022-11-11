h, m, s = map(int, input().split())
ogTime = h * 3600 + m * 60 + s
aFewMomentsLater = int(input())
endTime = (ogTime + aFewMomentsLater) % (24*60*60)
h = endTime // 3600
endTime -= h * 3600
m = endTime // 60
endTime -= m * 60
s = endTime
print(h, m ,s)