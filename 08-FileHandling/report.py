import re  # module for regular expressions

# File containing the shopping report
email_file = 'report.txt'

# Read the content of the file
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# Regular expression pattern for euro amounts
pattern = r'€\d+'

# Extract euro amounts from the email
amounts = re.findall(pattern, email)

# Calculate the total purchases
total = 0
for amount in amounts:
    total += float(amount[1:])  # Remove the euro symbol and convert to float

# Print the result
print(f"Total money spent: €{total:.2f}")
