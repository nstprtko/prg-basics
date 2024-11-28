# Function to find smallest and largest values and their positions
def find_min_max(array):
    # Initialize smallest and largest with the first element of the array
    min_val = array[0][0]
    max_val = array[0][0]
    min_position = (0, 0)
    max_position = (0, 0)
    
    # Iterate through the array to find the min and max values
    for i in range(len(array)):
        for j in range(len(array[i])):
            # Check if the current element is smaller than the current min
            if array[i][j] < min_val:
                min_val = array[i][j]
                min_position = (i, j)
            # Check if the current element is larger than the current max
            if array[i][j] > max_val:
                max_val = array[i][j]
                max_position = (i, j)

    return min_val, min_position, max_val, max_position

# Given 2D array
array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Find the smallest and largest values and their positions
min_val, min_pos, max_val, max_pos = find_min_max(array)

# Print the results
print(f"Smallest value: {min_val} at position {min_pos}")
print(f"Largest value: {max_val} at position {max_pos}")
