def sum_natural(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    
    return total_sum

print(sum_natural(10))