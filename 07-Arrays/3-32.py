# Function to swap the first and last rows
def swap_rows(array):
    # Swap the first and last rows
    array[0], array[-1] = array[-1], array[0]

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

# Swap the first and last rows
swap_rows(array)

# Print the array after swapping
print("\nArray After Swapping First and Last Rows:")
for row in array:
    print(row)
