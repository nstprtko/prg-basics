employees=[("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

formatted = list(map(lambda emp: f'{emp[0].upper()}, {emp[1]}', employees))

print('\n'.join(formatted))