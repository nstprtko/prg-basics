#ATM programme

balance_status = 1000
current_pin_code = '1234'
attempt = 0

while attempt < 3 :
    entered_pin = input('Enter your pin : ')
    if entered_pin == current_pin_code :
            print ('Succes')
            break

    else :
            attempt +=1
            print ('Unsuccesful, try again')

            if attempt == 3 :
                print('You have exhausted your tries')

while True :
    command = input ('What do you want to do?(Deposit / Withdraw / Show the balance/ Check PIN / Change PIN)')
    if command == 'Deposit' :
        deposit_amount= int(input('Enter the sum you want to deposit :'))
        balance_status += deposit_amount 
        print(f'You have deposited {deposit_amount}')
        print(f'Current account status is {balance_status}')

    elif command == 'Withdraw':
        withdrawal_amount  = int(input('Enter withdrawal amount :'))
        if withdrawal_amount <= balance_status :
            balance_status -= withdrawal_amount
            print(f'You have withdrawed {withdrawal_amount}')
            print(f'Your current account status is {balance_status}')
        else :
            print('You dont have enough money')


    elif command == "Show the balance" :
        print(f'Your balance is {balance_status}') 


    elif command == "Check PIN" :
        print (f'Your PIN is {current_pin_code}')


    elif command == "Change PIN " :

        new_pin = input('Enter new  4 digit pin :')
        if new_pin.isdigit() and len(new_pin) == 4: 
             current_pin_code = new_pin
             print('Your PIN has been changed')
        else :
             print('Enter 4 digit PIN')

    elif command == "Exit" :
        print('Goodbye')
        break






 