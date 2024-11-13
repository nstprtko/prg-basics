def f(expression):
    expression_str = str(expression)
    parts = expression_str.split()
    result = int(parts[0])
    for i in range(1, len(parts), 2):
        operator = parts[i]
        number = int(parts[i+1])

        if operator == '+':
            result += number

        elif operator == '-':
            result -= number

    return result
        





    
print(f('2 + 3 + 9 - 4'))