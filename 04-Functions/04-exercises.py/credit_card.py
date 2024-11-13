def hide(credit_card):
    credit_card_str = str(credit_card)# transform inputed into a string
    first_part = credit_card_str[:4]# take the first 4 digits of the converted string
    last_part = credit_card_str [-4:]#take last 4 digits of the string
    middle_part = credit_card_str[4:-4] # take the middle part, basicaly what stands between 

    blurred_number = first_part + middle_part.replace(middle_part, "*" * len(middle_part)) + last_part
# we add all the parts into one. notice how we use replce function. 
# very mindful, very demure
# we assign middle part the new value 
# middle_part. -> new value
# replace with (what was before, what do we want now * how many times we want it)
    return blurred_number