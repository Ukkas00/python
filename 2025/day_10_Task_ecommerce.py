# Provide register and login to user
# During register ask the user if he/she is buyer or seller
# In login after login successfull give user choices according to user's type
# If buyer : 1. View all products 2. Purchase a product 3. View bills
# If seller : 1. View products 2. Add product 3. View bills


import json


#-------------------------Main function--------------------------------------------
def main():

    user_input = input('Select the Type of user: 1. Buyer 2. Seller \n')
    if user_input == '1':
        buyer()
    elif user_input == '2':
        seller()
    else:
        print("Invalid input!")


#-------------------------Login & Register function------------------------------------
def login(user_type):
    user_choice = input("Enter a choice: 1. Register 2. Login \n")

    if user_choice == '1':
        while True:
            user_username = input("Enter your username: ")
            user_password = input("Enter your password: ")
            user_confirm_password = input("Confirm your password: ")

            if user_password == user_confirm_password:
                print("Registered successfully")

                user_dict_data = {
                    'username': user_username,
                    'password': user_password,
                    'type': user_type
                }

                user_json_data = json.dumps(user_dict_data)

                with open('Database/users.txt', 'a') as f:
                    f.write(user_json_data + '-')
                break
            else:
                print('Passwords do not match. Try again.')

    elif user_choice == '2':
            user_username = input("Enter your userName: ")
            user_password = input("Enter your password: ")

            f = open('Database/users.txt', 'r')
            user_data = f.read()
            f.close()

            list_user_data = user_data.split('-')
            list_user_data = user_data.split('-')
            if '' in list_user_data:
                list_user_data.remove('')
            
            for i in list_user_data:
                user_dict_data = json.loads(i)
                if user_dict_data.get('username') == user_username and user_dict_data.get('password') == user_password:
                    print("Login Successful !")
                    return user_dict_data['username'] # it check user name and it match give True other wise it give false
                    
            else:    
                print("Invalid username or password") 
                return None       
    else:
        print('Invalid input!')
        

#-------------------------Buyer function--------------------------------
def buyer():
    username = login('buyer')
    if username:
        while True:
            print("\nBuyer Options:")
            print("1. View all products")
            print("2. Purchase a product")
            print("3. View bills")
            print("4. Logout")
            choice = input("Enter your choice: ")


            # To view All the produts 
            if choice == '1':
                with open('Database/product.txt', 'r') as f:
                    product_data = f.read()
                
                list_product_data = product_data.split('-')
                if '' in list_product_data:
                    list_product_data.remove('')

                if list_product_data:
                    for i in list_product_data:
                        product = json.loads(i)
                        print(f"*****products:*****\n")
                        print(f"productName: {product['productName']}")
                        print(f"productName: {product['price']}")
                        print(f"productName: {product['quantity']}")
                        print('===============================')
                else:
                    print("No products found.")


            elif choice == '2':

                #shows lissted products
                with open('Database/product.txt', 'r') as f:
                    product_data = f.read()
                
                list_product_data = product_data.split('-')
                list_product_data.remove('')

                if list_product_data:
                    for i in list_product_data:
                        product = json.loads(i)
                        print(f"*****products:*****\n")
                        print(f"productName: {product['productName']}")
                        print(f"price: {product['price']}")
                        print(f"quantity: {product['quantity']}")
                        print('===============================')
                else:
                    print("No products found.")
                
                # buy products logics
                f = open('Database/product.txt', 'r')
                buy_data = f.read()
                f.close()  
                list_bill_data = buy_data.split('-')
                if '' in list_bill_data:
                    list_bill_data.remove('')
                list_bill_data.remove('')

                products = []
                for idx, i in enumerate(list_product_data):
                    product = json.loads(i)
                    products.append(product)  
                    print(f"{idx + 1}. productName: {product['productName']} - Price: {product['price']} - Quantity: {product['quantity']}")


                        #CODE HERE
                while True:
                    select_Input = input("Enter product index to purchase: \n")
                    if select_Input.isdigit():
                        index = int(select_Input)

                        if 1 <= index <= len(products):
                            selected_product = products[index - 1]
                            print(f"selectd products: {selected_product['productName']}")
                            break
                        else:
                            print('Out of range, try again!')
                    else:
                        print("Enter valid number!")
                
                while True:
                    quty = input(f"Enter qnty to buy (Available: {selected_product['quantity']}): ")
                    if quty.isdigit():
                        quty_int = int(quty)
                        if 1 <= quty_int <= selected_product['quantity']:
                            quty = quty_int
                            break
                    print('Give valid quty: ')
                
                selected_product['quantity'] -= quty

                f = open('Database/product.txt', 'w')
                for p in products:
                    json_str = json.dumps(p)
                    f.write(json_str + '-')
                
                f.close()

                total_price = selected_product['price'] * quty

                bill = {
                    'productName': selected_product['productName'],
                    'quantity': quty,
                    'price': total_price,
                    'buyer': username,
                    'seller': selected_product['sellerName'],
                }
                
                bill_dic_json = json.dumps(bill)
                f = open('Database/bill.txt', 'a')
                f.write(bill_dic_json + '-')

                print(f"successful! You purchase {quty} of {selected_product['productName']}. ")

                
            elif choice == '3':
                print("===== Your Bills=====")

                f = open('Database/bill.txt', 'r')
                bill_data = f.read()
                list_bill_data = bill_data.split('-')
                if '' in list_bill_data:
                    list_bill_data.remove('')
                list_bill_data = bill_data.split('-')
                list_bill_data.remove('')
                

                found = False
                for i in list_bill_data:
                        bill = json.loads(i)
                        if bill.get('buyer') == username:
                                print("\n-------------------")
                                print(f"Product: {bill['productName']}")
                                print(f"Quantity: {bill['quantity']}")
                                print(f"Price: {bill['price']}")
                                print(f"Seller: {bill['seller']}")
                                print("-------------------\n")
                                found = True
                if not found:
                            print("No bills found.")

            
            elif choice == '4':
                print("Logged out! \n")
                print("Visit Again! ")
                break
            else:
                print("Invalid choice. Give valid input! \n")

#-------------------------Seller-------------------------------------------
def seller():
    username = login('seller')
    if username:
        print(f"================Welcome {username}========================")
        while True:
            print("\nSeller Options:")
            print("1. View your products")
            print("2. Add a product")
            print("3. View bills")
            print("4. Logout")
            choice = input("Enter your choice: ")

            # Viewing products of sellers
            if choice == '1':
                f = open('Database/product.txt', 'r')
                product_data = f.read()
                f.close() 

                list_product_data = product_data.split('-')
                list_product_data.remove('')

                found = False
                for i in list_product_data:
                    product_dict_data = json.loads(i)
                    if product_dict_data.get('sellerName') == username:
                        print("***********Product Details:************")
                        print(f" Name    : {product_dict_data['productName']}")
                        print(f" Price   : {product_dict_data['price']}")
                        print(f" Quantity: {product_dict_data['quantity']}")
                        found = True
                if not found:
                        print(f"No product found")
                        


            # Adding Product
            elif choice == '2':
                product_name = input("Enter product name: \n")
                price = float(input("Enter price (In number) of your product: \n"))
                quantity = int(input("Enter Quantity (In number) of products: \n"))


                print('Add sucessfull!')
               
                seller_dic = {
                    'productName': product_name,
                    'price': price,
                    'quantity': quantity,
                    'sellerName': username
                }

                user_json_data = json.dumps(seller_dic)
                with open('Database/product.txt', 'a') as f:
                    f.write(user_json_data + '-')
                break
             

             #Bill get from buyer
            elif choice == '3':
                print("\n====================== Bills ==============================")

                f = open('Database/bill.txt', 'r')
                bill_list = bill_data.split('-')
                if '' in bill_list:
                    bill_list.remove('')

                bill_list = bill_data.split('-')
                bill_list.remove('')
                
                found = False
                for i in bill_list:
                    bill = json.loads(i)
                    if bill.get('seller') == username:
                        print(f"Product : {bill['productName']}")
                        print(f"Quantity: {bill['quantity']}")
                        print(f"Price   : {bill['price']}")
                        print(f"Buyer   : {bill['buyer']}")
                        found = True
                
                if not found:
                    print("No bill found! ")

                # For logOut
            elif choice == '4':
                print("Logged out! \n")
                print("Visit Again!")
                break
            
            else:
                print("Invalid choice. choose valid one.")

#-------------------------main start function--------------------------------
main()
