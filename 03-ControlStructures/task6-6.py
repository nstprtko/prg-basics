#Parkometer

hours_parked = int(input('Enter the amount of hours parked '))

if hours_parked <= 0 :
    print('Incorrect data')
    
elif hours_parked <= 2 :
    print('Your fee is 5 PLN')

elif hours_parked <=6 :
    print('Your parking fee is 15 PLN')

elif hours_parked > 6 :
    print('Your fee is 20 PLN')

