arr= [2, 6, 4, 9, 7]

def star(n):
    stars= n *'*'

    return stars

for num in arr:
    print(num, ':', star(num))

#print(arr[0],':', star(arr[0]))
#print(arr[1],':', star(arr[1]))