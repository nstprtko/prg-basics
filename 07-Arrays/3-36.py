# Function to convert 2D array to 1D
def convert_2d_to_1d(array_2d):
    # Initialize an empty list for the 1D array
    array_1d = []
    
    # Loop through each row of the 2D array
    for row in array_2d:
        # Add the elements of the current row to the 1D array
        array_1d.extend(row)  # Using extend to add all elements of row at once
    
    return array_1d

# Program to test the function with different 2D arrays
arrays_2d = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # 3x3 matrix
    [[10, 20], [30, 40], [50, 60]],  # 3x2 matrix
    [[100, 200, 300], [400, 500, 600]]  # 2x3 matrix
]

# Loop over each 2D array, convert it to 1D, and print the result
for i, array_2d in enumerate(arrays_2d, start=1):
    print(f"Original 2D Array {i}:")
    for row in array_2d:
        print(row)
    
    array_1d = convert_2d_to_1d(array_2d)
    
    print(f"Converted 1D Array {i}:")
    print(array_1d)
    print()  # Blank line between arrays
