import sys
a, b, c = map(int, sys.stdin.readline().split())
abclist = [a, b, c]
abclist.sort()
if a == b == c:
    print("2")
elif abclist[2] * abclist[2] == abclist[0] * abclist[0] + abclist[1] * abclist[1]:
    print("1")
else:
    print("0")