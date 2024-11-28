arr = [4,36,12,28,9,44,5]
#arr_sorted = sorted(arr)
#print(arr_sorted)

def buublesort(array):
    arr_sorted = sorted(array)
    
    arr_final = " ".join(map(str, arr_sorted))

    return arr_final

print(buublesort(arr))