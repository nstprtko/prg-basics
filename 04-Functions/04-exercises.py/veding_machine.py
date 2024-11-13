def vending_machine(amount_to_pay):
    coins_in_5 = amount_to_pay // 5# chech how many 5 zl coins we need 
    rest_from_5 = amount_to_pay % 5# find out the reminded amount
    coins_in_2 = rest_from_5 // 2 # how many 2 zl coins we need
    rest_from_2 = rest_from_5 % 2 # find the remainded amount
    coins_in_1 = rest_from_2 // 1 # find how many 1 zl coins we need, basically the resr
    # thats why we dont count the remainded amount

    result = coins_in_5 + coins_in_2 + coins_in_1

    return result

print(vending_machine(23))