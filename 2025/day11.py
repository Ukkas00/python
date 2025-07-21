# Requirements
# Provide register and login to user
# During register ask the user if he/she is buyer or seller
# In login after login successfull give user choices according to user's type
# If buyer : 1. View all products 2. Purchase a product 3. View bills
# If seller : 1. View products 2. Add product 3. View bills

users = {}
products = []
bills = []

def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter password: ")
    user_type = input("Are you a buyer or seller? (buyer/seller): ").strip().lower()
    if user_type not in ['buyer', 'seller']:
        print("Invalid user type.")
        return
    users[username] = {'password': password, 'type': user_type, 'bills': []}
    print("Registration successful.")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = users.get(username)
    if not user or user['password'] != password:
        print("Invalid credentials.")
        return

    print(f"Login successful. Welcome, {username} ({user['type']})!")
    if user['type'] == 'buyer':
        buyer_menu(username)
    elif user['type'] == 'seller':
        seller_menu(username)

def buyer_menu(username):
    while True:
        print("\nBuyer Menu:")
        print("1. View all products")
        print("2. Purchase a product")
        print("3. View bills")
        print("4. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_all_products()
        elif choice == '2':
            purchase_product(username)
        elif choice == '3':
            view_bills(username)
        elif choice == '4':
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def seller_menu(username):
    while True:
        print("\nSeller Menu:")
        print("1. View your products")
        print("2. Add product")
        print("3. View bills")
        print("4. Logout")
        choice = input("Enter your choice: ")
        if choice == '1':
            view_seller_products(username)
        elif choice == '2':
            add_product(username)
        elif choice == '3':
            view_bills(username)
        elif choice == '4':
            print("Logged out.")
            break
        else:
            print("Invalid choice.")

def view_all_products():
    if not products:
        print("No products available.")
        return
    print("\nAvailable Products:")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product['name']} - ${product['price']} (Seller: {product['seller']})")

def purchase_product(buyer):
    view_all_products()
    if not products:
        return
    try:
        choice = int(input("Enter the product number to purchase: ")) - 1
        if 0 <= choice < len(products):
            product = products[choice]
            bill = {
                'buyer': buyer,
                'seller': product['seller'],
                'product': product['name'],
                'amount': product['price']
            }
            bills.append(bill)
            users[buyer]['bills'].append(bill)
            users[product['seller']]['bills'].append(bill)
            print(f"You purchased {product['name']} for ${product['price']}.")
        else:
            print("Invalid product number.")
    except ValueError:
        print("Please enter a valid number.")

def view_bills(username):
    user_bills = users[username]['bills']
    if not user_bills:
        print("No bills found.")
        return
    print("\nYour Bills:")
    for bill in user_bills:
        print(f"Product: {bill['product']}, Seller: {bill['seller']}, Buyer: {bill['buyer']}, Amount: ${bill['amount']}")

def view_seller_products(seller):
    seller_products = [p for p in products if p['seller'] == seller]
    if not seller_products:
        print("You have not added any products.")
        return
    print("\nYour Products:")
    for i, product in enumerate(seller_products, start=1):
        print(f"{i}. {product['name']} - ${product['price']}")

def add_product(seller):
    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        products.append({'name': name, 'price': price, 'seller': seller})
        print("Product added successfully.")
    except ValueError:
        print("Invalid price. Please enter a number.")

# Main Program Loop
def main():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

# Run the program
main()
