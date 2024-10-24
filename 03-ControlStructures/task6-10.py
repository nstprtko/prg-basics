dog_age = int (input('Enter your dog age'))
first_two_years = 10.5
if dog_age == 1 :
    print(f'Your dogs age is {first_two_years} years')

elif dog_age == 2 :
    print(f'Your dogs age is {2 * first_two_years} years')

elif dog_age > 2 :
    real_dog_age = (dog_age - 2)*4 + (2 * first_two_years)
    print(f'Your dogs age is {real_dog_age}')

    