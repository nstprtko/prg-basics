def sum_natural(n):
    total_sum = 0# initiate count
    for i in range(1, n + 1): # for variable in range from 1 to inputed
        total_sum += i# add all the numbers in range
    
    return total_sum

print(sum_natural(10))