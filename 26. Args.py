# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can be accept a varying amount of arguments

def add(num1,num2):
    sum= num1 + num2
    return sum


print("------------------------")


def add(*args):
    sum=0
    args=list(args)
    args[0]=0
    for i in args:
        sum=sum+i
    return sum


print(add(1,2,3,4,5,6))


