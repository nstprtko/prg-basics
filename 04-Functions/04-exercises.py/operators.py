def f(number1, number2, operator): # ask to provide 3 arguments
    if operator == '+': # check each operator and provide the needed function
        # that this operator does 
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    

print(f(2,3, '-'))