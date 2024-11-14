def f(n):
    result = ''# initiate an empty string
    for i in range(1, n + 1) :# for an argument in range from 1 to given number
        # remember that for proper range we need to add one to the higher limit
        i_str= str(i) # cnvert it to the string so that result is a line of numbers
        # and not a sum 
        result += i_str # write numbers from range to an initiated empty string
    return result

        
print(f(5))