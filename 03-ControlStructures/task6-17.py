hours = int(input('Enter the hours'))
minutes = int(input('Enter minutes'))

if hours > 12 :
    hours -= 12
    print(f'Time in format is {hours} : {minutes}')

else :
    print(f'Time in format is {hours} : {minutes}')