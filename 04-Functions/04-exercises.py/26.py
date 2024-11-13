def f(text):
    text_str = str(text)
    #letters = [char for char in text_str]
    #for letters in text_str :
        #redacted = letters.join('-')
    redacted = '-'.join(text_str)
    return redacted


print(f('x'))