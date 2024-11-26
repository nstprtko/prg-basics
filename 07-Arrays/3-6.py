arr = [15, 8, 31, 47, 2, 19]
sum = 0
count = len(arr)
i = 0
while i < len(arr):
    sum += arr[i]
    i +=1 

result = sum / count
print(result)