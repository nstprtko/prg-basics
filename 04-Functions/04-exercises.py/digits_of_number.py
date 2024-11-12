def sum_of_digits(number, even):
    number_str = str(number)
    total = 0

    for digit in number_str :
        digit = int(digit)

        if digit % 2 == 0 and even :
            total += digit
        elif digit % 2 != 0 and not even :
            total += digit

    return total

print(f'{sum_of_digits(2345,False)}')