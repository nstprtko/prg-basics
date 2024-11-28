# Function to swap the first and last columns
def swap_columns(array):
    for row in array:
        # Swap the first column (index 0) and last column (index -1)
        row[0], row[-1] = row[-1], row[0]

# Create a 3x5 2D array
array = [
    [1, 2, 3, 4, 5],  # First row
    [6, 7, 8, 9, 10],  # Second row
    [11, 12, 13, 14, 15]  # Third row
]

# Print the original array before swapping
print("Original Array:")
for row in array:
    print(row)

# Swap the first and last columns
swap_columns(array)

# Print the array after swapping
print("\nArray After Swapping First and Last Columns:")
for row in array:
    print(row)
