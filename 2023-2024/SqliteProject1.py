import sqlite3

connection = sqlite3.connect("aquarium.db")
cursor = connection.cursor()
#databse of fish already recorded
cursor.execute("INSERT INTO fish VALUES('Sammy','Shark',1)")
cursor.execute("INSERT INTO fish VALUES('Jamie', 'cuttlefish', 2)")
cursor.execute("INSERT INTO fish VALUES('schmingle', 'swordfish', 3)")
cursor.execute("INSERT INTO fish VALUES('fonk', 'swordfish', 3)")
cursor.execute("INSERT INTO fish VALUES('cat', 'cuttlefish', 2)")
cursor.execute("INSERT INTO fish VALUES('fingle', 'clownfish', 4)")
cursor.execute("INSERT INTO fish VALUES('nemo', 'clownfish', 4)")

#enter a new fish to the database
def EnterNewFish():
    NewFish = input("what is the new fish's name?")
    FishSpecies = input("what is the fishes species?")
    TankNumber = input("what is the tank number of the fish?")
    cursor.execute("INSERT INTO fish (name,species,tank_number) VALUES (?,?,?)",(NewFish, FishSpecies, TankNumber))
# search for a fish in the database
def SearchFish():
    TargetFishSpecies = input("what is the species of fish you want to find?")
    rows1 = cursor.execute("SELECT name, species, tank_number FROM fish where species =?", (TargetFishSpecies,),).fetchall()
# print all the fish 
def PrintFish():
    rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
    print(rows)

def menu():
    MenuInput = input("""
        MENU
____________________                    
1) Enter New Fish
2) Search for fish
3) See All Fish
____________________\n""")
    if MenuInput == "1":
        EnterNewFish()
    elif MenuInput == "2":
        SearchFish()
    elif MenuInput == "3":
        PrintFish()
    else:
        print("this isnt a valid input try again! :)")
        menu()
menu()