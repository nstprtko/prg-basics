facebook = input('Enter if this person uses facebook (yes/no):')
instagram = input('Enter if this person uses instagram (yes/no):')
twitter = input ('Enter is this person uses twitter (yes/no):')

if (facebook == 'yes ' and instagram == 'yes') or (facebook =='yes' and twitter == 'yes') or (instagram =='yes' or twitter == 'yes') :
    print("This person is a good influencer")

else :
    print("This person is a bad influencer")