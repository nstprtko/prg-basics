def is_in_range(n, range1_input, range2_input): # we need three arguments for work 
    #range1_input = input('enter lower range')
    #range2_input = input('enter higher range')

    if n in range(range1_input, range2_input): # check if n belongs to the range
        return True # if the condition is true, return true
    else :
        return False # if condition somewhy is false, return false
    
print(is_in_range(8, 4, 10))