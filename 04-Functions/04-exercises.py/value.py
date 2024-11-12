def is_in_range(n, range1_input, range2_input):
    #range1_input = input('enter lower range')
    #range2_input = input('enter higher range')

    if range1_input<= n <= range2_input:
        return True
    else :
        return False 
    
#print(is_in_range(8))