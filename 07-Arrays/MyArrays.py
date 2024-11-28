def second_largest(array):
    array_sorted = sorted(set(array), reverse=True)
    return array_sorted[1]

#print(second_largest([50, 20, 40, 50, 30, 50]))

def difference(array):
    array_sorted = sorted(set(array))
    smallest_number = array_sorted[0]
    array_reversed = array_sorted[::-1]
    largest_number = array_reversed[0]
    difference = largest_number - smallest_number

    return difference
#print(difference([50, 20, 40, 50, 30, 50]))

def median(array):
    array_sorted = sorted(array)
    n = len(array)
    if n%2 != 0:
        return array_sorted[n // 2]
    elif n%2 == 0:
        lower = array[n//2 -1]
        higher = array[n//2]
        median = (lower + higher)/2

        return median

#print(median([50, 20, 40, 50, 30, 50]))

def new_array(array):
    array_sorted = sorted(set(array))
    smallest_number = array_sorted[0]
    array_reversed = array_sorted[::-1]
    largest_number = array_reversed[0]
    return [smallest_number, largest_number]

#print(new_array([50, 20, 40, 50, 30, 50]))

def score(array):
    new = "-".join(map(str,array))

    return new
    
#print(score([50, 20, 40, 50, 30, 50]))
