def letter_appears(sentence, letter):# ask to have two parameters, otherwise it wont work
    letter_lower = letter.lower()
    sentence_lower = sentence.lower()
    count = 0 # initiate count, since we need to count the letters
    for char in sentence_lower: # for every character in sentence :
        if char == letter_lower : # compare if character is equal to inputted character
            count +=1 # if so, add 1 point to the count
    return count # give the result
        
    
sentence = ' Elle elle'
letter = 'e'
print(f'The sentence{sentence} is {letter_appears(sentence, letter)} letter {letter}')
