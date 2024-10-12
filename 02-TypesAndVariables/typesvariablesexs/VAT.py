amount = float(input("Input amount :"))
rounded_amount = round (amount, 2)
vat = 23
vat_amount = (vat / 100) * amount
rounded_vat_amount = round (vat_amount, 2)

print(f"Inputed amount is {amount}")
print(f"Rounded amount is {rounded_amount}")
print(f"VAT 23% amount is {rounded_vat_amount}")


