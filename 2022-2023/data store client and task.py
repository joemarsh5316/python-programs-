import time
import datetime
def openfile():

#these are called variables
    f = open("database.txt", "a")
    productID = input("what is the product ID? ")
    productname = input("what is the product name? ")
    productprice = float(input("what is the product price ext VAT? "))
    productpriceVAT = float(productprice * 1.20)
    productprice = str(productprice)
    productpriceVAT = str(productpriceVAT)
    productlocation = input("where is the product stored in the warehouse")
    e = datetime.datetime.now()
    date2 = (e.strftime("%d/%m/%y"))
    time2 = (time.strftime("%H:%M"))
    date = (date2, time2)
    date = str(date)
#provides variables to be used in further code

#these write to the file to create a database 
    f.write("| productID: ")
    f.write(productID)
    f.write(" | Name: ")
    f.write(productname)
    f.write(" | product price: ")
    f.write(productprice)
    f.write(" | product price inc VAT: ")
    f.write(productpriceVAT)
    f.write(" | date and time of edit / add: ")
    f.write(date)
    f.write(" | \n")
#uses said code to then append the database file

def searchcontents():
    f = open("database.txt", "r")
    choice = input("how do you want to search for the product: 1: product ID or 2: product name? ")
    if choice == "1":
        productID = input("what is the product ID? ")
        with open("database.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.find(productID) != -1:
                    print(line)
                else:
                    print("item could not be found")
    elif choice == "2":
        productName = str(input("what is the name of the product? "))
        with open("database.txt", "r") as f:
            lines = f.readlines()
            y = 0
            for line in lines:
                if line.find(productName) != -1:
                    print(line)
                    y = 1
                else:
                    next
            if y == 1:
                next
            else:
                print("item could not be found")
    else:
        print("this is not a choice")
        searchcontents()
#this allows the client to choose what variable they want to search from



def menu():
    choice = input(" 1) view dataset\n 2) add new products\n 3) search products\n")
    print(choice)
    
    if choice == "1":
       f = open("database.txt", "r")
       contents = f.read()
       print(contents)
       
    elif choice == "2":
        openfile()
        
    elif choice == "3":
        searchcontents()
     

# this creates a menu to search through the database
while True:
    menu()

