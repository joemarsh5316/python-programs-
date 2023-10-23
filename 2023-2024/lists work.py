F1Teams = ["Ferrari","Williams","Haas","Racing Point"]
drivers = ["sebastian Vettel", "Charles Leclerc", "Kevin Magnussen","Lando Norris"]
wages = ["21 million", "17 million","3 million", "5 million"]
print("Current bonus Payment.", F1Teams[0])
print("Current rival is", F1Teams[1])


def listchange():
    locals; change0 = F1Teams.__delitem__(3)
    global Change01 
    Change01= F1Teams.insert(3, "Aston Martin")
    print(F1Teams)
listchange()


def listappend():
    print("Two more teams have been added!")
    F1Teams.append("Red Bull")
    F1Teams.append("Mercedes")
    print(F1Teams)
listappend()



def appendmenu():
    print("\n",F1Teams)
    input1 = int(input("what team do you want to change from 1-5?\n"))
    F1Teams.__delitem__(input1)
    TeamAdd = input("what team do you want to add?")
    F1Teams.insert(TeamAdd)
    print(F1Teams)
appendmenu()
