# Initialize the number of rows and columns
rows = 7
columns = 7

# Print the lottery coupon
for i in range(1, rows + 1):
    for j in range(columns):
        # Calculate the number to print based on the row and column
        number = (i - 1) + j * rows + 1
        print(f'{number}', end=' ')
    print()  # Move to the next line after each row