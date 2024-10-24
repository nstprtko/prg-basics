EAN = input('Enter EAN-13 :')

if len(EAN) == 13 and EAN.startswith("590") :
    print('Article number is correct and polish')

elif len(EAN) == 13:
    print('Article number is correct')

else :
    print('Incorrect number')