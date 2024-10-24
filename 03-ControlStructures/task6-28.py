# Initialize the first two terms of the Fibonacci sequence
fibonacci_sequence = [0, 1]

# Generate the Fibonacci sequence up to the 20th term
for i in range(2, 20):
    next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_term)

# Print the first 20 terms of the Fibonacci sequence
print("First twenty words of the Fibonacci sequence:")
for term in fibonacci_sequence:
    print(term, end=' ')
    