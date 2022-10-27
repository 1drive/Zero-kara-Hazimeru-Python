N = int(input())
N -= 1
pw = input()
ans = 0
orda = ord('a')
for alphabet in pw:
    df = ord(alphabet) - orda
    if df > 0:
        ans += (df)*26*(26**N-1)//(25)+df
    ans += 1
    N -= 1
print(ans)