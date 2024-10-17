#Write a program that prints the number of dice rolled and the value True if the number rolled is 1 or 6. 

import random

dice_roll = random.randint(1,6)
is_dice_roll = dice_roll == 1 or dice_roll == 6
print({dice_roll})
print({is_dice_roll})