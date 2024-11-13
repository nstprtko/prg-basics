def f(product_code):
    product_code_str = str(product_code)
    sum = int(product_code_str[0]) + int(product_code_str[1]) + int(product_code_str[2])
    remainder = sum % 7
    if remainder == int(product_code_str[3]):
        return True
    else :
        return False
    
print(f('1114'))