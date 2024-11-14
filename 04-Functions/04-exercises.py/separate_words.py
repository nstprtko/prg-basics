def f(sentence):# ask for an argument
    sentence_str = str(sentence) # turn it into a string
    cleared = sentence_str.replace(' ','') # we use replace function in following way
    #where_we_replace.replace("what we want to replace "," what we want to see in result" )
    
    return cleared

print(f('its cameron.the franchise.im trapped'))