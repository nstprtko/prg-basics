import csv 

csv_file = 'province.csv'
txt_file = 'vehicle.txt'

province_dict = {}# initialize an empty dictionary
with open(csv_file, 'r') as file1: # open csv file
    for line in file1: # for each line in file
        letter, province = line.strip().split(',')
        # we spilt the line by coma, so that we have two values
        province_dict[letter] = province # define the form for province dict 


vehicle_count = {} # initialize an empty dict 
for province in province_dict.values():
    # for new value province in dictionary 
    vehicle_count[province] = 0
    # initialize dictionary form and say its 0
with open(txt_file, 'r') as file2: # open txt file
    for line in file2: # for every line
        registration = line.strip() # clean up data
        if registration and registration[0] in province_dict:
            # check if the registration line is empty and then ask for the first index in province_dict

            province = province_dict[registration[0]]
            # take the value province and assighn it to the proper value from dict
            vehicle_count[province] +=1 
            # for every province add up 1

for province, count in vehicle_count.items(): 
    # acces key and value in dict vehicle count
    print(f'{province}: {count}')


