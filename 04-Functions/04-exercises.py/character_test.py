import character

sentence = str(input('enter your sentence'))
letter = str (input('enter the letter'))

print(f'Letter {letter} appears {character.letter_appears(sentence, letter)}times')
# again we call function in form of {module.function(arguments)}
# module name is the name of a file where function is stored