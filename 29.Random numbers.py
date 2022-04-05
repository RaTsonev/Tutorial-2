import random

x = random.randint(1,6) #random int number from 1 to 6
y = random.random() #random float number
print(x)
print(y)
print("-----------------------------------")
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)
print("-----------------------------------")
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)
