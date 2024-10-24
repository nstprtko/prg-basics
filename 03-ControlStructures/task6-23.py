# Read a number from the user
number = int(input("Enter a number: "))

# Generate and print the multiplication table from 1 to 10
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")