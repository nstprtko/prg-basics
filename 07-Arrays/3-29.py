def create_2d_arr(x, y):
    array =[]
    
    for _ in range(x):
        row = []
        for _ in range(y):
            row.append(0)
        array.append(row)
    return array
    
array = create_2d_arr(3, 5)

for row in array:
    print(row)


