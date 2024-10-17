# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')

# Convert letters to their Unicode code point values
first_letter_code = ord(first.upper())  # Ensure it's uppercase for correct ASCII value
last_letter_code = ord(last.upper())    # Same for the last letter

# Calculate the number of letters between the two
number_of_letters = abs(last_letter_code - first_letter_code) - 1

print(f'Between {first} and {last} are {number_of_letters} letter(s)')