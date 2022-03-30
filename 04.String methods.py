name = "John Smith"
print(len(name))
#len() ->  shows us the lenth of the name "John Smith"
print(name.find("m"))
#name.find("") ->  shows us the index number of the searched letter [6]
print(name.capitalize())
#name.capitalize() ->  turns the first lowercase letter into uppercase
print(name.upper())
#name.upper() -> turns all letters into uppercase
print(name.lower())
#name.lower() -> turns all letters into lowercase
print(name.isdigit())
#name.isdigit() -> it shows us if it is digit i.e. numbers
print(name.isalpha())
#name.isalpha() -> checks if it contains only letters i.e. the console will return False bcs it contains one space
print(name.count("o"))
#name.count("") -> turns back how many times the letter(in this case "o") is mentioned
print(name.replace("o","w"))
#name.replace("","") -> the first chosen letter (in this case "o") is replaced with the second chosen letter(in this case "w")
print(name*3)
#name*3 -> muliply 3 times the name