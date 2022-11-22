X, K = map(int, input().split())
snowmans = [0]
if K * 1.75 <= X:
    snowmans.append(K * 1.75 * 1000)
if K * 3.5 <= X:
    snowmans.append(K * 3.5 * 1000)
if K * 7 <= X:
    snowmans.append(K * 7 * 1000)
print(int(max(snowmans)))