limit = int(input())
current = int(input())
if current - limit <= 0:
    print("Congratulations, you are within the speed limit!")
elif 1 <= current - limit <= 20:
    print("You are speeding and your fine is $100.")
elif 21 <= current - limit <= 30:
    print("You are speeding and your fine is $270.")
elif 31 <= current - limit:
    print("You are speeding and your fine is $500.")
