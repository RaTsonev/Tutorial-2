# list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti"]
food[0]="sushi"
#here we replace index=0 i.e pizza with sushi

print(food[0])
#print the food with index=0
food.append("ice cream")
#add new word to the list
food.remove("hotdog")
#remove a word from the list
food.pop()
#remove last word from the list
food.insert(0,"cake")
#insert the word "cake" to the place index=0
food.sort()
#sort all list words alphabetically
food.clear()
#clar all words from the list
for x in food:
    print(x)
#here we list all words from food list
print("-------------------------")
