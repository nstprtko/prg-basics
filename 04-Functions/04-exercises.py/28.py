def f(dice):
    max_streak = 0
    current_streak = 1
    for i in range(1, len(dice)):
        if dice[i]== dice[i-1]:
            current_streak += 1
        else :
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 1

    max_streak = current_streak + 1
    return max_streak

print(f('1234444555'))

