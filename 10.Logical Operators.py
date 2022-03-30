#logical operators (and, or, not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside: "))
if temp >= 18 and temp <= 27:
    print("The temperature is good today")
    print("Go outside!")
elif temp < 18 or temp > 27:
    print("The temperature is bad today")
    print("Stay inside")

