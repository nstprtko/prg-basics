translation = {
    'computer': 'komputer',
    
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

input = str(input("enter word:"))

if input in translation :
    print(f'translation of {input} is {translation[input]}')

else :
    print('the translation is not available')