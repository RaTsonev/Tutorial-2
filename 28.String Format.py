# str.format() = option method that gives users more control when displaying outputs

animal = "cow"
item = "moon"
print("The "+animal+" jumped over the"+item)
print("The {0} jumped over the {1}".format("cow","moon"))  #keyword argument
print("The {1} jumped over the {0}".format(animal,item)) #positional argument
print("----------------------------------")
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) # no needen't to declated the values
print("The {animal} jumped over the {animal}".format(animal="cow",item="moon"))
text = "The {} jumped over the {}"
print(text.format(animal,item))

print("----------------------------------")
name = "Bro"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}.Nice to meet you".format(name))
print("Hello, my name is {:>10}.Nice to meet you".format(name)) # last name "Bro" is to the point
print("Hello, my name is {:^10}.Nice to meet you".format(name)) # the word "Bro" is in the middle of the empty space
print("----------------------------------")
number=3.14
print("The number pi is {:.2f}".format(number)) # print first 2 digits after the decimal
print("----------------------------------")
number=1000
print("The number is {:b}".format(number)) #binary representation of the number
print("The number is {:o}".format(number)) #octave number representation of the number
print("The number is {:x}".format(number))
print("The number is {:E}".format(number))
print("The number is {:E}".format(number))


