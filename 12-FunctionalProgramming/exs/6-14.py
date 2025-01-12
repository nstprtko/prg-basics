bottles=[508,500,512,499,492,511,503,476,501,509]

lower_limit = 500 - (2/100 *500)
upper_limit = 500 + (2/100 *500)

incr = list(filter(lambda x: x> upper_limit or x< lower_limit, bottles))
percentage = (len(incr)/len(bottles))* 100

print(f"Bottle capacity:    500ml")
print(f"Filling tolerance:  2%")
print(f"Filled bottles:     {', '.join(map(str, bottles))}")
print(f"Incorrectly filled: {percentage:.0f}%")