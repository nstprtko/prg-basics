def number_of_words(variable):
    splitted = variable.split()
    return (len(splitted))

def ordered(variable):
    splitted = variable.split()
    array_order= sorted(splitted, key=len, reverse= True)
    return array_order

def alphabet(variable):
    splitted = variable.split()
    array_alph = sorted(splitted)
    return array_alph

