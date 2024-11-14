#def f(palindrome):

    #cleaned_sentence = ''.join(char.lower() for char in palindrome if char.isalnum())# build a cleared sentence without spaces(join) 
    #with all the lower characters that applies to every element in sentence 

    #if cleaned_sentence == cleaned_sentence[::-1]:
        #return True

    #else:
        #return False

#print(f("A man, a plan, a canal, Panama"))

def f(palindrome):
    cleaned =''
    for char in palindrome:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]
        
    
print(f("A man, a plan, a canal, Panama"))
   
    