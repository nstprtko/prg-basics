pin = '1234'
attempt=0

while attempt < 3 :
    entered_pin = input('Enetr pin ')
    if entered_pin == pin :
            print ('Succes')
            break

    else :
            attempt +=1
            print ('Unsuccesful, tru again')

            if attempt == 3 :
                print('stop')

        


 
    

