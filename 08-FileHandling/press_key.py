file_name = 'it_company.csv'

lines_to_show = 5
start_line = 0


with open(file_name, 'r') as file:
    lines= file.readlines()

for i in range(lines_to_show):
    print(lines[i])
start_line = lines_to_show
    

print(start_line)
print("\nEnter Enter:")
input()
while start_line % 5 == 0:         
    while start_line <=len(lines):
        
        start_line = start_line + lines_to_show
        for i in range(start_line, start_line + 5):
            print(lines[i])
    

print(start_line)
print("\nEnter Enter:")
input()




