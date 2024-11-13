def f(detector):
    count = 0
    max_count = 0

    for entry in detector:
        if entry == '+':
            count +=1

        elif entry == '-':
            count -=1
        
    if count >= 3:
        return True
    else :
        return False

    

print(f('++-+-+-'))