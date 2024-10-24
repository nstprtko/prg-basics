# Read a decimal number from the keyboard
decimal_number = int(input("Enter a decimal number: "))

# Initialize an empty string to store the binary number
binary_number = ""

# Use a loop to repeatedly divide the number by 2
while decimal_number > 0:
    remainder = decimal_number % 2  # Get the remainder
    binary_number = str(remainder) + binary_number  # Add the remainder to the binary string
    decimal_number = decimal_number // 2  # Update the number by dividing by 2

# Output the binary number
print(f"The binary number is: {binary_number}")