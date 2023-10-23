
def car_search():
    modelinput = input("what model is that car?")
    file = open("cardatabase.txt", "r+")
    lines = file.readlines()

    for line in lines:
        splitted = line.split(",")

        if splitted[1] == modelinput:
            print("CAR FOUND")
            break

def new_customers():
    input1 = input("what is the customer's name?")
    input2 = input("what is the customer's address?")
    input3 = input("what is the customer's dob?")
    input4 = input(input1,input2,input3) ("\n are these details correct?")
    if input4 == "yes":
        print("customer added!")
        file1 = open("customer_database.txt", "w+")
        file1.write(input1,input2,input3)

def customer_search():
    nameinput = input("what is the name of the customer?")
    dobinput = input("what is the dob of the customer?")
    file = open("cardatabase.txt", "r+")
    lines = file.readlines()

    for line in lines:
        splitted = line.split(",")

        if splitted[1] == nameinput and dobinput:
            print("CUSTOMER FOUND")
            break

    file.close()

def new_car():
    input1 = input("what is the car's make?")
    input2 = input("what is the car's colour?")
    input3 = input("what is the car's model?")
    print(input1,input2,input3)
    input4 = input("\n are these details correct?")
    if input4 == "yes":
        print("car added!")
        with open("cardatabase.txt", "a+") as file:
            file.write(f"{input1},{input2},{input3}\n")

def menu():
    menu_input = input("""
    MENU
---------------------
1) Add a car         |
2) Car search        |
3) Add customer      |
4) Customer search   |
---------------------\n""")
    if menu_input == "1":
        new_car()
    elif menu_input == "2":
        car_search()
    elif menu_input == "3":
        new_customers()
    elif menu_input == "4":
        customer_search()
    else:
        print("this isnt the correct input try again! :)")
        menu()

menu()  
