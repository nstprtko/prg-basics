def f(number):
    
    number_str = str(number)
    sum = 0
    for char in number_str :
        if char == char :
            char_int = int(char)
            sum =+ char_int

    return sum

print(f(1027))