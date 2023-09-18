firstname = "Joseph"
lastname = "Marsh"
fulllegalname = "Joseph James Marsh"
nickname1 = "Marshy"
nickname2 = "Joe"
hobbies = "swimming, jiu jitsu, martial arts, GYM, gaming"
gaffalocation = "Middlesbrough, Oremsby"
age = "16"

def menu():
    print("what name do you want to know? ")

    choice = input("1) first name\n 2) last name\n 3) full legal name\n 4) nickname1\n 5) nickname2\n 6) what hobbies do i do\n 7) where i live\n 8) how old i am\n")

    if choice == "1":
       print(firstname)

    elif choice == "2":
        print(lastname)
        
    elif choice == "3":
        print(fulllegalname)

    elif choice == "4":
        print(nickname1)

    elif choice == "5":
        print(nickname2)

    else:
        print("choice not found")
        
    while True:
        menu()

    if 
