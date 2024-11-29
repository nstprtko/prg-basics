def read(name):
    with open(name) as file:
        content = file.read()
    return content

file_content = read('pets.txt')
file_words = file_content.split()
number = 0
for word in file_words:
    number+=1 

print(file_content)
print(number)