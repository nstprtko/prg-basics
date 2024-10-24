# Loop through numbers from 1 to 30
for number in range(1, 31):
    if number % 3 == 0 and number % 5 == 0:
        print('BINGO')  # Divisible by both 3 and 5
    elif number % 3 == 0:
        print('THREE')  # Divisible by 3
    elif number % 5 == 0:
        print('FIVE')  # Divisible by 5
    else:
        print(number)  # For other numbers, just print the number