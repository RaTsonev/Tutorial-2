#set = collection which is unordered, unindexed. No duplicate value

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
print("-------------------------")
utensils.update(dishes)  #dishes are added to utensils
for x in utensils:
    print(x)
print("-------------------------")
dishes.update(utensils)  #utensils are added to dishes
for x in dishes:
    print(x)
print("-------------------------")
dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)
print("-------------------------")
print(utensils.difference(dishes)) # dishes difference utensils items
print("-------------------------")
print(utensils.intersection(dishes))
