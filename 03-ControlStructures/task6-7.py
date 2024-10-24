#ask about age

age = int(input('Enter your age :'))

if age < 0 :
    print ('You havent been born yet')

elif age < 13 :
    print ('Child')

elif age < 19 :
    print ('Teen')

elif age < 64 :
    print ('Adult')

else :
    print ('Older')