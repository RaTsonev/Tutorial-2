# function = a block code which is executed only when it is called

def hello():
    print("Hello!")
    print("Have a nice day!")


hello() # call the function
print("-------------------------")

def hello(name):
    print("Hello "+name)
    print("Have a nice day!")


hello("Bro") # call the function
print("-------------------------")

def hello(name):
    print("Hello "+name)
    print("Have a nice day!")


hello("Dude") # call the function
print("-------------------------")

def hello(name):
    print("Hello "+name)
    print("Have a nice day!")


name = "Mike"
hello(name) # call the function
print("-------------------------")


def hello(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")


hello("John","Smith",21)  # call the function