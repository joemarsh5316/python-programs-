import pandas as pd
teamnames = 'teamnames.csv'
df = pd.read_csv('players.csv')
def teamcreate():
    Tname = input("Enter name of team: ")
    Pname = pd.read_csv("players.csv",usecols=["player names"])
    while Tname == "":
        Tname = input("Enter name of team: ")
    for x in range (6):
        print(df)
        choice = input("choose your player:")
    while Tname == "":
        if players > 6:
            print("the maximum players is 6")
    teamnames.loc[len(teamnames.index)] = [Tname,Pname,True]
    teams.to_csv("teamnames.csv", index = False)
teamcreate()
