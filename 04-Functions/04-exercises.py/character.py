def letter_appears(sentence, letter):# ask to have two parameters, otherwise it wont work
    count = 0 # initiate count, since we need to count the letters
    for char in sentence: # for every character in sentence :
        if char == letter : # compare if character is equal to inputted character
            count +=1 # if so, add 1 point to the count
    return count # give the result
        
    
#sentence = ' Hello world'
#letter = 'e'
#print(f'The sentence{sentence} is {letter_appears(sentence, letter)} letter {letter}')
