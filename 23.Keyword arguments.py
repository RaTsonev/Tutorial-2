#keyword argument = arguemnts preceded by an identifier when we pass them to a function.
#                   The order of the arguments doesn't matter, unlike positional argiments.
#                   Pyhon knows the name of the arguments that our function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello("John", "Willian", "Smith")
print("--------------------------------")
def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(first="John", middle="Willian",last="Smith")