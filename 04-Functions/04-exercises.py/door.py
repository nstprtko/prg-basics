def f(detector):
    count = 0#initiate count
    max_count = 0

    for entry in detector:# for each varuable entry in line detector
        if entry == '+': # check if entry = +
            count +=1# if so, add + 

        elif entry == '-': # check if entry = -
            count -=1 # if so substract one 
        
    if count >= 3: # after each checking add or substract 1 from the count
        # if we  have three people in one room or 3 pluses in a room in a row or in the same time
        return True # return True if so
    else :
        return False

    

print(f('++-+-+-'))