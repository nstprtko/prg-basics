number_of_products = int(input('Enter number of purchased products :'))
price_of_products = float(input('Enter total price of the product :'))

total_price = number_of_products * price_of_products

if number_of_products > 2 :
    discounted_products = number_of_products - 2
    discount = 0.25 * price_of_products * discounted_products
    total_price -= discount

print(f'Total amount to pay {total_price:.2f} PLN')
    