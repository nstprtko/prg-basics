#def f(number):# ask for one argument
# when we want to count something or have a sum, we initiate variable to which we will write this count to    
    #number_str = str(number)# convert to string to be able to run for 
    #sum = 0# inititate count
    #for char in number_str :# check every character 
       # if char == char : # try to find repeated characters
            #char_int = int(char) # if found, convert them to int to be able to run sum
           # sum += char_int # write sum of those numbers to the variable

    #return sum



def f(number):
    number_str = str(number)
    sum = 0
    for char in number_str.set(char)>0:
        if number_str.count(char)>1:
            sum += int(char)

    return sum
print(f(2055))