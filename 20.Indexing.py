#index operator [] = gives access to a sequence's element(str,list,tuples)

name = "bro Code"
if(name[0]).islower():
    name = name.capitalize()
print(name) #change the letter with index=0 from lowercase to uppercase
print("-------------------")
name = "bro Code!"
first_name=name[0:3].upper()
last_name=name[4:].lower()
last_character = name[-1] #first element from the end to the beginning

print(first_name) #print the first name(from index=0 to index=3 with uppercases
print(last_name)  #print the last name(from index=4 to the end with lowercases
print(last_character) #print the first element from the end to the beginning