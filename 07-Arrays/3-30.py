# Function to create and print a multiplication table
def create_multiplication_table(rows, cols):
    # Initialize a 2D array with the specified dimensions
    table = [[0 for _ in range(cols)] for _ in range(rows)]

    # Fill the table with multiplication values
    for i in range(rows):
        for j in range(cols):
            table[i][j] = (i + 1) * (j + 1)  # Multiplying row and column indices

    return table

# Define the size of the table
rows = 5
cols = 5

# Create and print the multiplication table
multiplication_table = create_multiplication_table(rows, cols)

# Print the table
for row in multiplication_table:
    print(row)
