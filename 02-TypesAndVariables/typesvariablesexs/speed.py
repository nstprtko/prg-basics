#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
#Write a program that checks whether the vehicle speed entered from the keyboard is correct.

car_speed = int(input('Enter the car speed :'))
is_car_speed = car_speed >= 40 and car_speed <= 140
print(f'Car speed is within the limit {is_car_speed}')