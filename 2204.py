while True:
    T = int(input())
    if T == 0:
        break
    else:
        arr = []
        for i in range(T):
            arr.append(input())
        arr.sort(key=lambda k: k.lower())
        print(arr[0])