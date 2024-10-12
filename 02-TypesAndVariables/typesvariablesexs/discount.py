 #Write a program that allows you to enter the product price and discount. 
 # Print the product price, discount, discounted product price, 
 # and the difference between the product price before and after the discount.
 #  Print all prices with two decimal places. 

product_price = float (input("Enter the price :"))
discount = float (input("Enter discount :"))
discounted_price = (discount / 100) * product_price
price_difference = product_price - discounted_price

print (f"Product price is {product_price:.2f}" )
print (f"Discount is {discount:.2f} %")
print(f"Discount is {discounted_price:.2f}")
print(f"Difference between prices is {price_difference:.2f}")