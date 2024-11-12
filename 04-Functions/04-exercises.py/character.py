def letter_appears(sentence, letter):
    count = 0
    for char in sentence:
        if char == letter : 
            count +=1
    return count 
        
    
#sentence = ' Hello world'
#letter = 'e'
#print(f'The sentence{sentence} is {letter_appears(sentence, letter)} letter {letter}')
