# Function to transpose a matrix
def transpose_matrix(m):
    # Create an empty matrix for the transpose
    transposed = []
    
    # Iterate over the columns of the original matrix and create the rows of the transposed matrix
    for i in range(len(m[0])):  # Iterate over columns of the original matrix
        row = []
        for j in range(len(m)):  # Iterate over rows of the original matrix
            row.append(m[j][i])  # Append element at m[j][i] to the new row
        transposed.append(row)
    
    return transposed

# Function to print a 2D array in a readable format
def print_2d_array(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))  # Print each row in a single line

# Program to transpose and print matrices
matrices = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # 3x3 matrix
    [[1, 2], [3, 4], [5, 6]],  # 3x2 matrix
    [[1, 2, 3, 4], [5, 6, 7, 8]]  # 2x4 matrix
]

# Loop over each matrix, transpose it, and print the result
for i, matrix in enumerate(matrices, start=1):
    print(f"Original Matrix {i}:")
    print_2d_array(matrix)
    transposed = transpose_matrix(matrix)
    print(f"Transposed Matrix {i}:")
    print_2d_array(transposed)
    print()  # Blank line between matrices
