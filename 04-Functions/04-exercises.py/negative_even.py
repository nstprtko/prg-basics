def negative_even_numbers(lower_range, higher_range):# ask for 2 parameters 
    count = 0 # initiate count, because we need to output the amount
    
    for digit in range(lower_range, higher_range + 1) :# create variable digit
        # check if digit is in the range
        # for range to be proper, dont forget to add 1 to higher range

        if digit < 0 and digit % 2 == 0:# if variable is negative and even :
            count +=1# add 1 to the count

    return count

print(negative_even_numbers(-5, 6)) 