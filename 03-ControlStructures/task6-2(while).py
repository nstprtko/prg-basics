text = "Hello, how many vowels are in this sentence?"
vowels = "aeiouAEIOU"
count = 0
index = 0

while index < len(text):
    if text[index] in vowels:
        count += 1
    index += 1

print("Number of vowels:", count)