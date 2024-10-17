# Input an integer from the user
decimal_number = int(input("Enter an integer number: "))

# Convert the decimal number to binary and hexadecimal
binary_representation = bin(decimal_number)  # bin() converts to binary
hexadecimal_representation = hex(decimal_number)  # hex() converts to hexadecimal

# Print the results
print(f"The binary representation of {decimal_number} is: {binary_representation}")
print(f"The hexadecimal representation of {decimal_number} is: {hexadecimal_representation}")