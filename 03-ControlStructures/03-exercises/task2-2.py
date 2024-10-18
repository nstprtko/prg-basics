###
# A program for checking clothing sizes
# S: Small size, M: Medium size, L: Large size
# XL: Extra large size or Incorrect symbol (if entered symbol
# dirrerent than S, M, L, XL)
#
size = input('Enter size symbol: ')

if size == 'S' or size == 's':
    print('S: Small size')
elif size == 'M' or size == 'm':
    print('M: Medium size')
elif size == 'L' or size == 'l':
    print(' L: Large size')
elif size == 'XL' or size == 'xl':
    print('XL: Extra large')

else:
    print('Incorrect symbol')
