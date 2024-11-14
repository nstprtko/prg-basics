def f(dice):
    max_streak = 0# initiate an empty variable
    current_streak = 1# we start counting streak from 1 because we meet a number once
    for i in range(1, len(dice)): # for i in range from 1 to the length of inputed
        if dice[i]== dice[i-1]:# if index and previous index are same
            current_streak += 1# add one to a current streak
        else :
            if current_streak > max_streak:# current streak is always bigger than max streak
                max_streak = current_streak # update variables 
            current_streak = 1

    max_streak = current_streak + 1 
    return max_streak

print(f('1234444555'))

