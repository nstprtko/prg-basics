import re

username=str(input("Enter your username:"))
password=str(input("Enter your password:"))

username_pattern = r'^[A-Za-z][A-Za-z0-9_]{5,}$'
password_pattern = r'^[A-Za-z0-9_]{8,}$'

username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

if username_match and password_match:
    print('True')

else:
    print('False')