def f(binary):
    binary_str= str(binary)
    for char in binary_str :
        if char != '1' and char != '0':
            return False
        
    return True
        
print(f('1011'))