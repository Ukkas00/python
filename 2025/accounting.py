# Requirements
# Provide user login and register
# Provide user access to add balance, view balance and withdraw balance after login
# User's should be only able to work with their own balance data only
# Important - Use oop(Better program structure), File handling(Data storage), Git and Github for Version Control

import os
import hashlib

USERS_FILE = "users.txt"

def register(username, password):
    if os.path.exists(f"users/{username}.txt"):
        return False, "Username already exists."
    with open(USERS_FILE, "a") as f:
        f.write(f"{username},{(password)}\n")
    with open(f"users/{username}.txt", "w") as f:
        f.write("0")  # balance is 0 initially
    return True, "User registered successfully."

def login(username, password):
    if not os.path.exists(USERS_FILE):
        return False, "No registered users."
    with open(USERS_FILE, "r") as f:
        lines = f.readlines()
    for line in lines:
        user, pwd = line.strip().split(",")
        if user == username and pwd == (password):
            return True, "Login successful."
    return False, "Invalid credentials."
class UserAccount:
    """Class to handle user account operations like balance management."""  
    def __init__(self, username):
        self.username = username
        self.file_path = f"users.txt"
    
    def get_balance(self):
        with open(self.file_path, "r") as f:
            return float(f.read().strip())

    def add_balance(self, amount):
        balance = self.get_balance()
        balance += amount
        with open(self.file_path, "w") as f:
            f.write(str(balance))
        return balance

    def withdraw_balance(self, amount):
        balance = self.get_balance()
        if amount > balance:
            raise ValueError("Insufficient funds.")
        balance -= amount
        with open(self.file_path, "w") as f:
            f.write(str(balance))
        return balance
    
    print("Welcome to laxmi banking service")
def main():


 True:
 print("\n1. Register\n2. Login\n3. Exit")
choice = input("Enter choice: ")

    if choice == "1":
        username = input("New username: ")
        password = input("New password: ")
        success, msg = register(username, password)
        print(msg)

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        success, msg = login(username, password)
        print(msg)
        if success:
            user = User(username)
            while True:
                print(f"\n--- Welcome, {username} ---")
                print("1. View Balance\n2. Add Balance\n3. Withdraw\n4. Logout")
                op = input("Choose an option: ")
                try:
                    if op == "1":
                        print(f"Your balance: ${user.get_balance():.2f}")
                    elif op == "2":
                        amount = float(input("Enter amount to add: "))
                        bal = user.add_balance(amount)
                        print(f"New balance: ${bal:.2f}")
                    elif op == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        bal = user.withdraw_balance(amount)
                        print(f"New balance: ${bal:.2f}")
                    elif op == "4":
                        break
                    else:
                        print("Invalid option.")
                except ValueError as e:
                    print("Error:", e)

    elif choice == "3":
        print("Goodbye!")
        break