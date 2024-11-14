def f(x,y):
    result = 0# initiate count
    for i in range(x,y): # for variable in given range 
        if i % 2 == 0 and i % 3 == 0 and i % 4 != 0 :# check every condition 
            result += i# add those numbers together 

    return result

print(f(1, 20))