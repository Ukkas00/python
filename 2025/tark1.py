#list if valid username
valid_username = ['user_name1','user_name2','user_name3','user_name4','user_name5',]
# Ask for the username
username = input('enter your username:')
# Check if the username is valid 
if username in valid_username:
    print("Login Successful")
else:
    print("Invalid username")