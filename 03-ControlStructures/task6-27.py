i = 6
while i >= 0:
    j = 1
    while j <= 3:
        print(f'{i+j}', end=' ')
        j += 1
    print()  # To move to the next line after each row
    i -= 3  # Decrease i by 3 to go to the next row