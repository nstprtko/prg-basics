def third_power(arr):

    third_power = list(map(lambda num : num ** 3, arr))
    return ', '.join(map(str,third_power))

arr = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10,
       11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

result = third_power(arr)
print(result)