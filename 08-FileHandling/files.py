import re
pattern = r'\W\w{4}'
file_name = "files.txt"
with open(file_name, 'r') as file:
    file_content = file.readlines()

for line in file_content:
    line_match = re.search(pattern, line)
    if line_match:
        print(line.strip())