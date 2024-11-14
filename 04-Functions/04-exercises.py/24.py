def f(expression):
    expression_str = str(expression) # convert to str to run for
    parts = expression_str.split() # split inputted to parts
    # it splits to spaces by default
    # if we want to split smth by other character, we should specify it in brackets and ""
    result = int(parts[0])# convert first digit into int
    for i in range(1, len(parts), 2):# for every i in specific range
        #range from 1 to length of parts(not included) with a step of 2
        operator = parts[i]# since we start with 1 with a step 2, it only acceses odd
        # indexes, which are exactly the operator indexes
        number = int(parts[i+1])#number is even indexes converted to a number

        if operator == '+':
            result += number

        elif operator == '-':
            result -= number

    return result
        





    
print(f('2 + 3 + 9 - 4'))