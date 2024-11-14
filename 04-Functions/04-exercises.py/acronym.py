def f(name):# ask for an argument
    #return ''.join(word[0] for word in name.split())
    name_str= str(name)# convert inputed to a string
    name_split = name_str.split() #break string into words
    result =''# initiate an empty string where we will write letters to
    for word in name_split:# for each word in the splitted variable
        result += word[0] # write every first character to an empty variable
        

    return result



print(f('Cor In Ium'))