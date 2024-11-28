arr = [15, 38, 7, 23, 14]

def occurs(number, array):
    for element in array:
        if element == number:
            print ('Number:', number)
            print('Array:', " ".join(map(str,array)))
            print(f'Result: number {number} appears in the array')
        
    return False
        
    

print(occurs(23, arr))
#print('Number')