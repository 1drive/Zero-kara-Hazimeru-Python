while True:
    member = list(map(str, (input().split())))
    member[1], member[2] = int(member[1]), int(member[2])
    if member == ["#", 0, 0]:
        break
    if member[1] > 17 or member[2] >= 80:
        print(member[0], "Senior")
    else:
        print(member[0], "Junior")