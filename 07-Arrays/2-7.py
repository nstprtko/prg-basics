import random

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr10 =[4,0,3]
#15-element array filled with zeros
arr11 = [0 for i in range(15)]
#an array with integer values in the range of <1,30>
arr12 = [i for i in range(1,31)]
#20-element array filled with 0 or 1 randomly
arr13 = [random.randint(0,1) for _ in range (20)]
#two dimensional array with five rows and two columns filled with False
arr14 = [
    [False, False],
        [False, False],
        [False, False],
        [False, False],
        [False, False]
         ]


print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print(arr10)
print(arr11)
print(arr12)
print(arr13)
print(arr14)
for row in arr14:
    print(''.join(map(str, row)))


