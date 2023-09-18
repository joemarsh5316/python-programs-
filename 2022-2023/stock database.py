def EnterproductID():
    productID = str(input("what is the 7 digit product ID: "))
    productName = str(input("what is the products name: "))
    department = str(input("what category is the product in: "))
    warehouseLocation = str(input("Where is the product stored in the warehouse: "))
    stockAmount = str(input("How much is in stock: "))
    priceIncVAT = str(input("What is the price incuding VAT: "))
    priceExVAT = str(input("What is the price excluding VAT: "))
    lengthID = len(productID)



    if lengthID != 7:
        print("Enter a 7 digit ID")
    else:
        next

        f = open("Database.txt" , "a")
        f.write("| ID: ")
        f.write(productID)
        f.write(" | Name: ")
        f.write(productName)
        f.write(" | Department: ")
        f.write(department)
        f.write(" | Warehouse Location: ")
        f.write(warehouseLocation)
        f.write(" | Stock Amount: ")
        f.write(stockAmount)
        f.write(" | Price Ex VAT: ")
        f.write(priceExVAT)
        f.write(" | Price Inc VAT: ")
        f.write(priceIncVAT)
        f.write(" | \n")

        f.close()


with open('database.txt', 'w') as f:
    f.write('')

    f = open('filename.txt', 'a')
    f.write(input())
