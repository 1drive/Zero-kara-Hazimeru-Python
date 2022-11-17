while True:
    enc = input().strip()
    if enc == "END":
        break
    else:
        print(enc[::-1])