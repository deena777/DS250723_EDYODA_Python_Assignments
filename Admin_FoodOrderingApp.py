class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = None  # To be generated automatically
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

admins = []  # List to store admin objects
food_items = []  # List to store food item objects
admin_logged_in = None  # Initialize the logged-in admin as None

def generate_food_id():
    # Generate a unique food ID based on the length of the list
    return len(food_items) + 1

def admin_registration():
    username = input("Enter an admin username: ")
    password = input("Enter an admin password: ")
    admin = Admin(username, password)
    admins.append(admin)
    print("Admin registered successfully!")

def admin_login():
    global admin_logged_in
    username = input("Enter your admin username: ")
    password = input("Enter your admin password: ")
    for admin in admins:
        if admin.username == username and admin.password == password:
            admin_logged_in = admin
            print("Admin login successful!")
            return
    print("Invalid admin username or password. Admin login failed.")

def add_food_item():
    name = input("Enter the name of the food item: ")
    quantity = input("Enter the quantity (e.g., 100ml, 250gm, 4 pieces): ")
    price = float(input("Enter the price: Rs."))
    discount = float(input("Enter the discount in %: "))
    stock = int(input("Enter the stock amount: "))
    food_id = generate_food_id()
    food_item = FoodItem(name, quantity, price, discount, stock)
    food_item.food_id = food_id
    food_items.append(food_item)
    print("Food item added successfully with FoodID:", food_id)

def edit_food_item():
    food_id = int(input("Enter the FoodID of the food item to edit: "))
    for food_item in food_items:
        if food_item.food_id == food_id:
            print("Editing Food Item with FoodID:", food_id)
            name = input(f"Enter the new name ({food_item.name}): ") or food_item.name
            quantity = input(f"Enter the new quantity ({food_item.quantity}): ") or food_item.quantity
            price = float(input(f"Enter the new price ({food_item.price}): Rs.")) or food_item.price
            discount = float(input(f"Enter the new discount ({food_item.discount})%: ")) or food_item.discount
            stock = int(input(f"Enter the new stock amount ({food_item.stock}): ")) or food_item.stock

            food_item.name = name
            food_item.quantity = quantity
            food_item.price = price
            food_item.discount = discount
            food_item.stock = stock
            print("Food item edited successfully.")
            return

    print(f"No food item found with FoodID {food_id}.")

def view_food_items():
    if food_items:
        print("\nList of Food Items:")
        for food_item in food_items:
            print(f"FoodID: {food_item.food_id}, Name: {food_item.name}, Quantity: {food_item.quantity}, Price: Rs.{food_item.price}, Discount: {food_item.discount} %, Stock: {food_item.stock}")
    else:
        print("No food items found.")

def remove_food_item():
    food_id = int(input("Enter the FoodID of the food item to remove: "))
    for food_item in food_items:
        if food_item.food_id == food_id:
            food_items.remove(food_item)
            print(f"Food item with FoodID {food_id} removed successfully.")
            return

    print(f"No food item found with FoodID {food_id}.")

while True:
    print("\nFood Ordering App")
    if admin_logged_in is None:
        print("1. Admin Registration")
        print("2. Admin Login")
    else:
        print(f"Logged in as Admin: {admin_logged_in.username}")
        print("3. Add Food Item")
        print("4. Edit Food Item")
        print("5. View Food Items")
        print("6. Remove Food Item")
        print("7. Logout")

    print("8. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        admin_registration()
    elif choice == '2':
        admin_login()
    elif choice == '3':
        if admin_logged_in is not None:
            add_food_item()
        else:
            print("Admin login required to add food items.")
    elif choice == '4':
        if admin_logged_in is not None:
            edit_food_item()
        else:
            print("Admin login required to edit food items.")
    elif choice == '5':
        view_food_items()
    elif choice == '6':
        if admin_logged_in is not None:
            remove_food_item()
        else:
            print("Admin login required to remove food items.")
    elif choice == '7':
        admin_logged_in = None
        print("Admin logged out.")
    elif choice == '8':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
