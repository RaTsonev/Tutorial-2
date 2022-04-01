# Loop control statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

#break
while True:
    name = input("Enter your name: ")
    if name != "":
        break
print("-------------------------")

#continue
phone_number = "123-456-7890"
for i in phone_number:
    if i =="-":
        continue
    print(i, end="")
print("-------------------------")

#pass
for i in range(1,21):
    if i==23:
        pass
    else:
        print(i)
