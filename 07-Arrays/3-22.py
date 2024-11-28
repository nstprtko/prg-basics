import random
def rand_elem(array):
    index = random.randint(0, len(array)-1)
    element=array[index]
    return element
print(rand_elem([1, 2, 3, 4]))
print(rand_elem([1, 2, 3, 4]))