# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of kayword arguments


def hello(first,last):
    print("Hello "+first+ " "+last)


hello(first="Bro",last="Code")
print("--------------------------------")

def hello(**kwargs):
    print("Hello "+kwargs['first']+ " "+kwargs['last'])


hello(first="Bro",last="Code")
print("--------------------------------")

def hello(**kwargs):
    print("Hello "+kwargs['first']+ " "+kwargs['last'])
    for key,value in kwargs.items():
        print(value,end=" ")


hello(first="Bro",last="Code")