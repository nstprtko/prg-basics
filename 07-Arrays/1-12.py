categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = expenses.index(max(expenses))
expencive_category = categories[max_index]

print( expencive_category)
