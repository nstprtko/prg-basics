car_speed = int( input ('Enter your car speed :'))
speed_limit_min = 40
speed_limit_max = 140

if car_speed > speed_limit_max :
    print('Exceeded speed limit')

elif car_speed < speed_limit_min :
    print('Warning : invalid car limit')

else :
    print('Youre good to go' )