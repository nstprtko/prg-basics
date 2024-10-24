# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Read the value of N from the keyboard
N = int(input("Enter the number of leading prime numbers to find: "))

# Initialize a list to store prime numbers
primes = []
num = 2  # Starting from the first prime number

# Find the first N prime numbers
while len(primes) < N:
    if is_prime(num):
        primes.append(num)
    num += 1  # Move to the next number

# Print the leading prime numbers
print(f"The first {N} prime numbers are: {primes}")