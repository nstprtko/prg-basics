def is_binary(binary_number):
    binary_number_str = str(binary_number)# transform inputted into string to 
    # be able to check it contains
    if all(char in '01' for char in binary_number_str):
        #assign a new variable char
        # if all characters is binary_str are equal to 01 the output is true
        return True
    
    else:
        return False 
    
#print(is_binary('01110'))