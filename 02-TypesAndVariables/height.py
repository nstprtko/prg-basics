###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
cm_per_inch = 2.54
inches_per_foot = 12
height_in_inches = cm / cm_per_inch
height_in_feet = height_in_inches // inches_per_foot #wo a reminder
rest_of_the_inches = height_in_inches % inches_per_foot #remaining inches

print(f'I am {cm}cm tall, i.e. {height_in_feet} feet and {rest_of_the_inches} inches')