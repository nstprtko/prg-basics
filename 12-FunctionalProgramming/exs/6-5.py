def divisible(arr):
    result = list(filter(lambda num: num % 2 ==0 and num % 3==0, arr))
    return  result

arr = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10,
       11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

result = divisible(arr)
print(result)