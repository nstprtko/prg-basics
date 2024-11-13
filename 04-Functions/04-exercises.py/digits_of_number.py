def sum_of_digits(number, even):
    number_str = str(number)# convert to str to check the insides 
    total = 0 # initiate count, we will put the sum here later, so it also can be sum

    for digit in number_str : # check each character/digit in string
        digit = int(digit)# convert each character into number 

        if digit % 2 == 0 and even : # if the number is even and the parameter #2 IS TRUE
            total += digit # add those even digits 
        elif digit % 2 != 0 and not even : # if the number is odd and the parameter even is FAlSE
            total += digit # add those odd digits and write it as total/sum

    return total

print(f'{sum_of_digits(2345,True)}')