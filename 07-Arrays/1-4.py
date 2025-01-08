###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('last but one', len(arr)-2)
print('sum of the first and the last', arr[0] + arr[-1])

middle_index = len(arr) // 2

print('middle value',arr[middle_index])

for element in arr:
    print (element, end = ' ')
    
