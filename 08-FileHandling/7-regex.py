import re
vowels_pattern = r'[AOEUIaoeui]'
text = str(input("enter your text"))
vowels_match = re.findall(vowels_pattern, text)
if vowels_match:
    print(', '.join(vowels_match))

