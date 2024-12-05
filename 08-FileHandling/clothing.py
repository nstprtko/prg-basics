import csv

file_name = 'clothing.csv'
with open(file_name, mode="r", newline="", encoding="utf-8") as file:
    reader= csv.DictReader(file)
    for column in reader:
        if float(column['Price']) < 60 and float(column['Stock_Quantity']) < 40:
            print(column['Product_ID'],column['Product_Name'])