def identity_matrix(n):
    # Create a square matrix of size n x n
    matrix = []
    
    # Fill the matrix with 0's and 1's on the diagonal
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)  # Set diagonal elements to 1
            else:
                row.append(0)  # Set non-diagonal elements to 0
        matrix.append(row)
    
    return matrix

# Function to print a 2D array in a readable format
def print_2d_array(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))  # Print each row in a single line

# Main program to print three identity matrices
sizes = [3, 5, 8]
for size in sizes:
    print(f"Identity Matrix of size {size}:")
    matrix = identity_matrix(size)
    print_2d_array(matrix)
    print()  # Print a blank line between matrices
