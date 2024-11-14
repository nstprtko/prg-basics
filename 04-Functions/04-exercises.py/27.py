def f(product_code):
    product_code_str = str(product_code)# convert to a string
    sum = int(product_code_str[0]) + int(product_code_str[1]) + int(product_code_str[2])
    # convert 1-3 element to a int and sum it up 
    remainder = sum % 7 # the fourth digit is the remainder of sum / 7, which we 
    # count here 
    if remainder == int(product_code_str[3]):# if the counted remainder is the same as the fourth character in inputed code

        return True # then return true
    else :
        return False
    
print(f('1082'))