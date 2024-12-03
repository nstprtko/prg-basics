file_name = 'it_company.csv'

lines_to_show = 5
start_line = 0

# Read the file and store lines
with open(file_name, 'r') as file:
    lines = file.readlines()

# Display lines in chunks of 5
while start_line < len(lines):
    # Print the next set of lines
    for i in range(start_line, min(start_line + lines_to_show, len(lines))):
        print(lines[i], end='')  # Print each line without adding extra newlines

    start_line += lines_to_show  # Move to the next set of lines

    # Check if there are more lines to show
    if start_line < len(lines):
        print("\nPress Enter key to continue...")
        input()  # Wait for user input to continue