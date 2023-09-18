import csv
with open("movies.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "Protagonist"])
    writer.writerow([1, "lord of the Rings", "Frodo Baggins"])
    HarryPotter = writer.writerow([2, "Harry Potter", "Harry Potter"])
    Batman = writer.writerow([3, "Batman", "Bruce Wayne"])
    Deadpool = writer.writerow([4, "deadpool", "Wade wilson"])
    FightClub = writer.writerow([5, "fight club", "Tyler Durden / Jack Moore"])
    LOTR = ("lord of the Rings", "Frodo Baggins")
with open("movies.csv", "r") as file:
    print(LOTR, HarryPotter, Batman, Deadpool, FightClub)
    rowreader = input("what movie do you want to find out about?")
    reader = csv.reader(file)
    for row in reader:
        print(rows[3])
    
