###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
for i in range(2,11):
    n= 1/i
    rounded_n= round(n, 2)
    print(f'1/{i} = {rounded_n}')