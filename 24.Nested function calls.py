#nested function calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for tge next outer function

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)
