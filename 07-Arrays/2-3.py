# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

sum_food = monthly_expenses[0][0] + monthly_expenses[1][0] + monthly_expenses [2][0] + monthly_expenses[3][0]
sum_transport = monthly_expenses[0][1] + monthly_expenses[1][1] + monthly_expenses [2][1] + monthly_expenses[3][1]
sum_utilities = monthly_expenses[0][2] + monthly_expenses[1][2] + monthly_expenses [2][2] + monthly_expenses[3][2]
sum_all=0

# Calculates expenses
# Use loop statements
for row in monthly_expenses:
    for item in row:
        sum_all +=item


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',sum_food)
print('Transport:', sum_transport)
print('Utilities:',sum_utilities)
print('Week 1:', monthly_expenses[0][0] + monthly_expenses[0][1] + monthly_expenses[0][2])
print('Week 2:',sum(monthly_expenses[1]))
print('Week 3:',sum(monthly_expenses[2]))
print('Week 4:',sum(monthly_expenses[3]))
print('---------------')
print('TOTAL:',sum_all)