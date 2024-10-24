current_price = int (input('Input currrent product price :'))
previous_price = int (input('Input previous product price :'))

percentage_formula = (previous_price - current_price)/previous_price * 100 

print(f'Current product price is {current_price}'
      f'Previous product price is {previous_price}')

if percentage_formula >= 10 :
    print('Buy the product!'
          f'Product price reduced by {percentage_formula}% ')
    
else :
    print('You should wait longer.'
          f'Price reduced by {percentage_formula}%')
