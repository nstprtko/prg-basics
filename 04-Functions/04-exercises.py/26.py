def f(text):
    text_str = str(text)# convert to str
    #letters = [char for char in text_str]
    #for letters in text_str :
        #redacted = letters.join('-')
    redacted = '-'.join(text_str)# add - to text 
    return redacted


print(f('hello'))