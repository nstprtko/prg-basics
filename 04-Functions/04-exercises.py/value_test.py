import value

n = int(input('Enter the number:'))
range1_input = input('enter lower range')
range2_input = input('enter higher range')

print(f'Your number is {n}')
print(f'Number {n} is in {range1_input, range2_input}: {value.is_in_range(n, range1_input, range2_input)}') 