import csv

file_name = 'it_company.csv'
with open(file_name, mode="r", newline="", encoding='utf-8') as file:
    reader = csv.DictReader(file)
    print("GRAPHIC DESIGHNERS")
    print("==================")

    for row in reader:
        if row['Job Title']=='Graphic Designer':
            
            print(row['Last Name'], row['First Name'], row['Email'])