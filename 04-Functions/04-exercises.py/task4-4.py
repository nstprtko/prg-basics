# Define a function to calculate the sum of digits
def sum_of_digits(number):
    total = 0
    for digit in str(abs(number)):  # Convert to string to iterate over each digit
        total += int(digit)  # Convert each character back to integer and add to total
    return total

# Read a number from the keyboard
number = int(input("Enter a number: "))

# Calculate and print the sum of its digits
result = sum_of_digits(number)
print(f"The sum of the digits in {number} is {result}")