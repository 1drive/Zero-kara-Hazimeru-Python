from curses.ascii import isupper


A = input()
B = ""
for i in A:
    if i.isupper() == True:
        B += i.lower()
    else:
        B += i.capitalize()
print(B)