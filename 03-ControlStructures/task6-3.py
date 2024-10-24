###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
#light_switch1 = False # False - switch off, True - switch on
#light_switch2 = False

what_bulbs_are_lit = input('switch1 or switch2?')
bulbs_on = 0
if what_bulbs_are_lit == "switch1":
    bulbs_on += 1
if what_bulbs_are_lit == 'switch2':
    bulbs_on += 2
print(f'Bulbs lit are {bulbs_on}')