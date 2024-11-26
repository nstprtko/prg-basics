arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

count = " "
for item in arr:
    if len(item) > len(count):
        count = item

print(len(count))
print(count)

