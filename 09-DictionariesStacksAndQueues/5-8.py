# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

price = 0
# Calculate total cost
for item, quantity in cart.items():
    price += prices[item] * quantity

print(price)
