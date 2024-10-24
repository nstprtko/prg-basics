x = int(input('Enter x - coordinate'))
y = int(input('Enter y - coordinate'))

if x > 0 and y > 0 :
    print('Point is located in the first quadrant')

elif x > 0 and y < 0 :
    print('Point is located in the fourth quadrant')

elif x < 0 and y > 0 :
    print('Point is located in the second quadrant')

elif x < 0 and y < 0 :
    print('Point is located in the third quadrant')

if x == 0 :
    print('Point is located on y-axis')

if y == 0 :
    print('Point is located on x - axis')

if x == 0 and y == 0 :
    print('Point is (0;0)')



