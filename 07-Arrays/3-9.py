arr1 = ["water","book","sky"]
arr2= ["water","book","sky"]

def compare(array1, array2):
    len_array1 = len(array1)
    len_array2 = len(array2)

    
    if len_array1 != len_array2:
        return False

    for cell in range(len_array1):
        if array1[cell] != array2[cell]:
            return False

    return True 
    

print('Array 1:'," ".join(arr1))
print('Array 2:', " ".join(arr2))
if compare(arr1, arr2):
    print('arrays are the same')
else:
    print('arrays are not the same')


