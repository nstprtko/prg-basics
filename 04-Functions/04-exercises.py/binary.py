def is_binary(binary_number):
    binary_number_str = str(binary_number)
    if all(char in '01' for char in binary_number_str):
        return True
    
    else:
        return False 
    
#print(is_binary('01110'))