price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

sum_before = 0
sum = 0
print('Prices before sale')
for key, value in price_list.items():
    
    print(f'{key} : {value}')

sum_before += value
print(f'The price before{sum_before:.2f}')

for key, value in price_list.items():
    price_list[key] = value * 0.9

print("Prices after 10% discount:")

for key, value in price_list.items():
    
    print(f'{key} : {value}')

sum +=value
print(f'Sum of products after dicount {sum:.2f}')




        
       






