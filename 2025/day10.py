#Requriments 
#User should ne able to register or login
#In 



#module 
import json 



user_choice = input("Enter a choice: 1 for Register, 2 for Login: ")

if user_choice == "1":
	user_name = input("Enter a username: ")
	user_password = input("Enter a password: ")
	user_dict_data = {'username': user_name, 'password': user_password}
	with open("D:/PC/2025/user_data.txt", "r") as f:
		json_user_data = json.dumps(user_dict_data)
		f.write(json_user_data + "\n")
		f.close()

elif user_choice == "2":
	user_name = input("Enter your username: ")
	user_password = input("Enter your password: ")
	f = open(r"D:/PC/2025/user_data.txt", "r")
	user_datas = f.read()
	f.close()
	print (user_datas)
	
login_success = False
for line in user_datas.strip().split('\n'):
	try:
		user_record = json.loads(line)
		if user_record.get('username') == user_name and user_record.get('password') == user_password:
			print("Login successful")
			login_success = True
			break
	except json.JSONDecodeError:
		continue
if not login_success:
	print("Invalid input")