chess = []
current = input()
init = current
chess.append(current)
isValid = 0
for i in range(35):
    new = input()
    chess.append(new)
    if chess.count(new) >= 2:
        isValid += 1
    if (abs(ord(current[0])-ord(new[0])) == 2 and abs(int(current[1]) - int(new[1])) == 1) or (abs(ord(current[0])-ord(new[0])) == 1 and abs(int(current[1]) - int(new[1])) == 2):
        isValid += 0
    else:
        isValid += 1
    current = new
if (abs(ord(init[0])-ord(new[0])) == 2 and abs(int(init[1]) - int(new[1])) == 1) or (abs(ord(init[0])-ord(new[0])) == 1 and abs(int(init[1]) - int(new[1])) == 2):
    isValid += 0
else:
    isValid += 1
if isValid == 0:
    print("Valid")
else:
    print("Invalid")