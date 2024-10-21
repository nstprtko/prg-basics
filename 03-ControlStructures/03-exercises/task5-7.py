import time

# Get the countdown time from the user
seconds = int(input("Enter the number of seconds to count down: "))

# Start the countdown
while seconds > 0:
    if seconds == 5:
        print("five")
    elif seconds == 4:
        print("four")
    elif seconds == 3:
        print("three")
    elif seconds == 2:
        print("two")
    elif seconds == 1:
        print("one")
    else:
        # Print the number for all other seconds
        print(seconds)
    
    time.sleep(1)  # Pause for 1 second
    seconds -= 1

print("Time's up!")
