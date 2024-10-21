###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0 #початкове значення ячейки
i = 1 #стартовий поінт

# Calculate the sum of even numbers
while i <= N : #виконувати луп до того моменту коли і = н
    if i % 2 == 0: # сумувати тільки парні числа
        sum_even += i #додавати парні значення і
    i +=1 #



print(f"The sum of even numbers from 1 to {N} is: {sum_even}")