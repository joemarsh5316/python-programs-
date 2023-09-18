import json
import os
import random
database = None

'''
Database is a dictionary which is the unique product id mapped to Product class
Upon saving it turns the list of Product classes into a dictionary and saved it to a file
When loading it loads the saved dictionary's and create new product instances
'''

ID_LENGTH = 7

class Product:
    def __init__(self, name, identifier, department, warehouse, stock, price, vatPrice):
        self.name = name
        self.id = identifier
        self.department = department
        self.warehouse = warehouse
        self.stock = stock
        self.price = price
        self.vatPrice = vatPrice
        
    def up_stock(self, amount):
        self.stock += amount

    def down_stock(self, amount):
        self.stock -= amount

# Search for Product by partial name or id
def search_product():
    query = InputType("Enter a search query: ")
    # Checks if the query matches product id exactly
    if database.get(query):
        product = database.get(query)
        print("There are", product.stock, product.name, "'s in stock at", product.warehouse)
        return
    # Searches for product by partial name
    results = []
    for product in database.values():
        if query.lower() in product.name.lower():
            results.append(product)
    if len(results) > 0:
        print("Here are my search results:")
        for product in results:
            print(product.name, "has", product.stock, "in stock at", product.warehouse)
    else:
        print("No search results were found :/")
        
    

# Updates the stock of a product
def update_stock(increment = True):
    action = "increment" if increment else "decrement"
    product_id = InputType("Enter the product id to " + action + " in stock: ")
    amount = InputType("Enter the amount to " + action + ": ", int)
    product = database.get(product_id)

    # Calls the Product classes stock change methods
    if increment:
        product.up_stock(amount)
    else:
        product.down_stock(amount)

    save_database()
    print("The stock in", product.name, "was", action + "ed by", amount, ".")

def instance_product():
    name = InputType("Enter a name for the product: ")
    department = InputType("Enter a dapartment for the product: ")
    warehouse = InputType("Enter a warehouse for the product: ")
    stock = InputType("Enter the starting stock for the product: ", int)
    price = InputType("Enter the price for the product: ", float)
    identifier = generate_id()
    vatPrice = str(price * 1.2)
    # Creating new product class instance
    product = Product(name, identifier, department, warehouse, stock, price, vatPrice)
    database[identifier] = product
    save_database()
    print("The product", name, "has now been created.")

def generate_id():
    identifier = ''
    # Loop over until a unique idenfiter is generated 
    while True:
        for i in range(ID_LENGTH):
            identifier += str(random.randint(0, 9))
        if database.get(identifier) == None:
            break
        # Reset the value of identifier so it can generate a new one
        identifier = ''
    return identifier

def menu():
    print("\n1. Enter a new product")
    print("2. Search Product")
    print("3. Increment stock")
    print("4. Decrement stock")
    print("5. Quit")
    
    choice = InputType("Chooce a option from the menu: \n")
    if choice == "1":
        instance_product()
    elif choice == "2":
        search_product()
    elif choice == "3":
        update_stock(True)
    elif choice == "4":
        update_stock(False)
    elif choice == "5":
        quit()

def InputType(prompt, t = str):
    msg = input(prompt)
    while type(msg) != t:
        try:
            msg = t(msg)
        except:
            msg = input("Invald input! Please try again: ")
    return msg

def save_database():
    f = open("database.txt", "w")
    data = {}
    # Loops over each Product class turns it into a dictionary
    for p in database.values():
        data[p.id] = p.__dict__
    # Writes all product data to the file
    f.write(str(json.dumps(data)))
    f.close()

def load_database():
    global database
    # Create file is non existant
    if os.path.exists("database.txt") == False:
        (open("database.txt", "w+")).close()
    f = open("database.txt", "r")
    data = f.read()
    # Parses the data to json or empty array
    if data == "":
        data = {}
    else:
        data = json.loads(data)
    database = {}
    for key, value in data.items():
        product = Product(
            value['name'],
            value['id'],
            value['department'],
            value['warehouse'],
            value['stock'],
            value['price'],
            value['vatPrice'],
        )
        database[key] = product
    f.close()

load_database()
while True:
    menu()
