###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = 3
b = 4
c = 5

def triangle_area(a,b,c):
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

tr = triangle_area(a,b,c)

import math
d = 5
e = 12
f = 13

def triangle_area1(d,e,f):
    s1 = (d + e + f)/2
    area1 = math.sqrt(s1 * (s1 - d) * (s1 - e) * (s1 - f))
    return area1

tr1 = triangle_area1(d,e,f)


print(f'The area of ​​a triangle with sides 3, 4, 5 is {tr}')
print(f'The area of ​​a triangle with sides 5.12.13 is {tr1}')
print('The area of ​​a triangle with sides ... is ...')
