def AdminLogin():
    adminlogin = input("what is your username?")
    adminpassword = input("what is your password?")

    if adminlogin and adminpassword!=("Staff"):
        print("im sorry that is the incorrect password :(")

AdminLogin()

def openfile():
        f = open("database.txt", "a")
        IDnumber = input("what is the student ID? ")
        studentsurname = input("what is the students surname? ")
        studentfirstname = input("what is the students firstname? ")
        DOB = input("what is the date of birth? ")
        homeaddress = input("what is the students home address? ")
        homephonenumber = input("what is home phone number? ")
        genders = input("what is the students gender?")

        f.write("| IDnumber: ")
        f.write(IDnumber)
        f.write(" | Surname: ")
        f.write(studentsurname)
        f.write(" | Firstname: ")
        f.write(studentfirstname)
        f.write(" | students DOB: ")
        f.write(DOB)
        f.write(" | students home address: ")
        f.write(homeaddress)
        f.write(" | students home number: ")
        f.write(homephonenumber)
        f.write(" | students gender: ")
        f.write(genders)
        f.write(" | \n")

def searchcontents():
    f = open("database.txt", "r")
    choice = input("how do you want to search for the student: 1: student ID or 2: student name? ")
    if choice == "1":
        productID = input("what is the student ID? ")
        with open("database.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.find(productID) != -1:
                    print(line)
                else:
                    print("student could not be found")
    elif choice == "2":
        productName = str(input("what is the name of the student? "))
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
                print("student could not be found")
    else:
        print("this is not a choice")
        searchcontents()
def logout():
    while True:
        menu()

        if choice == "4":
            print("logged out ")
            break

def menu():
    choice = input(" 1) view student dataset\n 2) add new students\n 3) search students\n 4) logout\n")
    print(choice)
    
    if choice == "1":
        f = open("database.txt", "r")
        contents = f.read()
        print(contents)
       
    elif choice == "2":
        openfile()
        
    elif choice == "3":
        searchcontents()
        
    elif choice == "4":
        logout()
        print("logged out ")

    else:
        print("invalid")
        menu()
                
menu()


def logout():
    while True:
        menu()

        if choice == "4":
            print("logged out ")
            break

