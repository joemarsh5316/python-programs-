import sqlite3


connection = sqlite3.connect("cars.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE cars (Model TEXT, Miles FLOAT, Year Of Release INTERGER)")

NewCar = input("what is the car's model?")
CarMiles = input("what is the miles on the car?")
YearOfRelease = input("what is the year of realease?")

cursor.execute("INSERT INTO cars  (name,species,) VALUES (?,?,?)",(NewCar, CarMiles, YearOfRelease))