import character

sentence = str(input('enter your sentence'))
letter = str (input('enter the letter'))

print(f'Letter {letter} appears {character.letter_appears(sentence, letter)}times')