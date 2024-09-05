
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Initialize attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        # Return the cost of the shoe
        return self.cost

    def get_quantity(self):
        # Return the quantity of the shoes
        return self.quantity

    def __str__(self):
        # Return a string representation of the class
        return f"Shoe(country={self.country}, code={self.code}, product={self.product}, cost={self.cost}, quantity={self.quantity})"

#=============Shoe list===========
 # List to store Shoe objects
shoe_list = [] 

#==========Functions outside the class==============
def read_shoes_data():
    # Read data from file and create Shoe objects
    try:
        with open("inventory.txt", "r") as file:
            # Skip the first line
            next(file) 
            for line in file:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def capture_shoes():
    # Get user input and create a Shoe object
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = input("Enter cost: ")
    quantity = input("Enter quantity: ")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

def view_all():
    # Print all shoes in the list
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    # Find the shoe with the lowest quantity and update it
    lowest_qty_shoe = None
    lowest_qty = float('inf')
    for shoe in shoe_list:
        if int(shoe.quantity) < lowest_qty:
            lowest_qty = int(shoe.quantity)
            lowest_qty_shoe = shoe
    print(f"Shoe with lowest quantity: {lowest_qty_shoe.product} ({lowest_qty_shoe.quantity})")
    add_qty = input("Enter quantity to add: ")
    lowest_qty_shoe.quantity = str(int(lowest_qty_shoe.quantity) + int(add_qty))
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
    with open("inventory.txt", "w") as file:
        for line in lines:
            if line.strip().split(",")[1] == lowest_qty_shoe.code:
                file.write(f"{lowest_qty_shoe.country},{lowest_qty_shoe.code},{lowest_qty_shoe.product},{lowest_qty_shoe.cost},{lowest_qty_shoe.quantity}\n")
            else:
                file.write(line)

def search_shoe():
    # Search for a shoe by code
    code = input("Enter shoe code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            break
    else:
        print("Shoe not found!")

def value_per_item():
    # Calculate the total value of each shoe
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"Shoe: {shoe.product}, Value: {value}")

def highest_qty():
    # Find the shoe with the highest quantity
    highest_qty_shoe = None
    highest_qty = 0
    for shoe in shoe_list:
        if int(shoe.quantity) > highest_qty:
            highest_qty = int(shoe.quantity)
            highest_qty_shoe = shoe
    print(f"Shoe with highest quantity: {highest_qty_shoe.product} ({highest_qty_shoe.quantity})")

#==========Main Menu=============
while True:
    print("Welcome to the Shoe Store!")
    print("1. Load Shoes from File")
    print("2. Add a New Shoe")
    print("3. View All Shoes")
    print("4. Restock Shoes")
    print("5. Search for a Shoe")
    print("6. Calculate Total Value")
    print("7. Find Shoe with Highest Quantity")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again!")