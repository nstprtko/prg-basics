file_name = 'it_company.csv'

lines_to_show = 5
start_line = 0


with open(file_name, 'r') as file:
    lines= file.readlines()

while start_line < len(lines):
    for i in range(start_line,min(start_line  +lines_to_show, len(lines))) :
        print(lines[i], end='')

    start_line+=lines_to_show

    if start_line < len(lines):
        print("\nPress Enter")
        input()




