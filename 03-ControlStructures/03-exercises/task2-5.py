###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month <=3:
    quarter = 1
elif month <=6 and month > 3 :
    quarter = 2
elif month <=9 and month > 6 :
    quarter = 3


print(f'Month {month} is in quarter {quarter}')