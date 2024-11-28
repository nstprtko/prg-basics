def count(array, value):
    count = 0
    for element in array:
        if element > value:
            count +=1

    return count


arr=[2,3,5,7,8,10]
number = float(input('enter value'))
print(count(arr, number))

