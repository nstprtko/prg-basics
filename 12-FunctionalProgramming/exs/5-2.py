from functools import reduce

numbers = [2,4,6,3,7,5]
even = list(filter(lambda num: num % 2 == 0, numbers))
#sum = reduce(lambda acc, num : acc + num, even)
sum = sum(even)

print(sum)
