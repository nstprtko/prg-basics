def f(n):
    result = ''
    for i in range(1, n + 1) :
        i_str= str(i)
        result += i_str
    return result

        
print(f(5))