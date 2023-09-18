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
openfile()




def menu():
    
    choice = input(" 1) view student dataset\n 2) add new students\n 3) search students\n")
    print(choice)
    
    if choice == "1":
       f = open("database.txt", "r")
       contents = f.read()
       print(contents)
       
    elif choice == "2":
        openfile()
        
    elif choice == "3":
        searchcontents()
        
    def login():
        adminlogin = input("what is your username?")
        adminpassword = input("what is your password?")
        if adminlogin and adminpassword == ("staff", "staff"):
            menu()   

while True:
    menu()







