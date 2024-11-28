arr1=[1, 5]
arr2=[1, 2, 3, 4]
def subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False
        
    else:
        return True

print(subset(arr1,arr2))
        
    
