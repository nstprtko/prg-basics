###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input('Enter the letter')
print(letter)

number_from_string = int("20303")
print(number_from_string)

binary_string = bin(304)[2:]  # Removes the '0b' prefix from the binary representation
print(binary_string)

hexadecimal_string = hex(304)[2:]  # Removes the '0x' prefix from the hexadecimal representation
print(hexadecimal_string)

euro_unicode = ord("€")
print(euro_unicode)

absolute_value = abs(-17)
print(absolute_value)