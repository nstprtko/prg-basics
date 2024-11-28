arr = [7,9,2,4,5,6]
even_numbers=[]
odd_numbers=[]
for element in arr:
    if element % 2 ==0:
        even_numbers += [element]
    elif element %2  !=0 :
        odd_numbers += [element]

result = even_numbers + odd_numbers

print(" ".join(map(str,result)))