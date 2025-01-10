# List of names
names = ['James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']

# Use sorted() with a lambda function to sort by length
sorted_names = sorted(names, key=lambda name: len(name))

# Print the result
print("Sorted names by length:", sorted_names)
