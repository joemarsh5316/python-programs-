import sqlite3

#variables
connection = sqlite3.connect("aquarium.db")
cursor = connection.cursor
cursor.execute("create table fish (name TEXT, Species Text, Tank_number INTERGER)")
cursor.execute("INSERT INTO fish VALUES('Sammy','Shark',1)")
cursor.execute("INSERT INTO fish VALUES('Jamie', 'cuttlefish', 7)")

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
cursor.close
print(rows)

