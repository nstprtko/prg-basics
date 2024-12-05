file_name =  str(input("File name:"))


with open(file_name, "r") as file:
    count_lines = 0
    count_characters = 0
    count_words = 0
    file_content = file.read()
    file_lines = file_content.splitlines()
    
    
    for line in file_lines:
        count_lines +=1
        stripped_line = line.replace(" ", "").replace("\n", "")
        count_characters +=len(stripped_line)
        
    count_words = len(file_content.split())


    print(f"Number of lines :{count_lines}")
    print(f"Number of characters: {count_characters}")
    print(f"Number of words:{count_words}")

