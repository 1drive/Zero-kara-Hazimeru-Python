arr = list(map(int, input().split()))
arr.sort()
diff01 = abs(arr[0] - arr[1])
diff12 = abs(arr[1] - arr[2])
if diff01 == diff12:
    tmp = arr[0] - diff12
    print(tmp)
elif diff01 == diff12 * 2:
    print(arr[0] + diff12)
elif diff01 * 2== diff12:
    print(arr[1] + diff01)