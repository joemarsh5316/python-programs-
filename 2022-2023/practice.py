import csv 
with open("practice.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


