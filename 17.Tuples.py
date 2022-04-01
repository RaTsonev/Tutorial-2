# tuples = collection which is ordered and unchangeable used to a group together related data

student = ("Bro",21,"male")
print(student.count("Bro"))
print(student.index("male"))
print("-------------------------")
for x in student:
    print(x)
#print all elements in the student
print("-------------------------")
if "Bro" in student:
    print("Bro is here!")