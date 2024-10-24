# Set the correct PIN
correct_pin = "0805"

# Initialize the number of attempts
attempts = 0

# Allow up to 3 attempts
while attempts < 3:
    entered_pin = input("Enter your PIN: ")
    
    if entered_pin == correct_pin:
        print("Correct PIN. Access granted.")
        break
    else:
        attempts += 1
        print("Incorrect PIN. Try again.")
        
    if attempts == 3:
        print("Card blocked. Too many incorrect attempts.")