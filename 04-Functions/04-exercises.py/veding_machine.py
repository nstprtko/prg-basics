def vending_machine(amount_to_pay):
    coins_in_5 = amount_to_pay // 5
    rest_from_5 = amount_to_pay % 5
    coins_in_2 = rest_from_5 // 2
    rest_from_2 = rest_from_5 % 2
    coins_in_1 = rest_from_2 // 1

    result = coins_in_5 + coins_in_2 + coins_in_1

    return result

print(vending_machine(23))