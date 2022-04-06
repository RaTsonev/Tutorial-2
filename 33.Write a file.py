
text = "\nAdd some text"

with open('33.test.txt', 'a') as file:
    file.write(text)

# 'w' -> write in file as overwrite the text
# 'a' i.e append-> write in file as add new text