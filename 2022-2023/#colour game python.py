import random

def ranking(cpoints,hpoints):
        if cpoints > hpoints:
            print("\n\nYou lost!")
        elif cpoints < hpoints:
            print("\n\nYou win!")
        else:
            print("\n\nYou drew!")


while True: 
    cpoints = 0
    hpoints = 0
    colour = ["red","blue","yellow","green","white"]

    game = int(input("\nWelcome to the colour game! Choose player 1:\n1)computer\n2)Player\n3)Exit\nEnter number: "))
    if game == 1:
        
        for x in range (1,11):
            cguess= random.randint(1,5)
            print("\nRound ",x," of 10!")
            guess = int(input("Guess where the computer is hiding!\n1)Red\n2)Blue\n3)Yellow\n4)Green\n5)White\nEnter guess: "))
            if guess == cguess:
                 print("\nYou were right! The computer picked" ,colour[(cguess-1)])
                 hpoints += 1
            elif guess > 5:
                print("\nPick number 1 - 5")
                x -=1
            else:
                print("\nYou were wrong! The computer picked" ,colour[(cguess-1)])
                cpoints += 1
        ranking(cpoints,hpoints)



    elif game == 2:
            for x in range (1,11):
                cguess= random.randint(1,5)
                print("\nRound ",x," of 10!")
                guess = int(input("Hide from the computer!\n1)Red\n2)Blue\n3)Yellow\n4)Green\n5)White\nEnter spot: "))
                if guess == cguess:
                     print("\nYou were found! The computer picked" ,colour[(cguess-1)])
                     cpoints += 1
                elif guess > 5:
                    print("\nPick number 1 - 5")
                    x -=1
                else:
                    print("\nYou werent found! The computer picked" ,colour[(cguess-1)])
                    hpoints += 1
            ranking(cpoints,hpoints)
                


    elif game == 3:
        break
    
    else:
        print("\nPick legitimate option")
import random

def ranking(cpoints, hpoints):
    if cpoints > hpoints:
        print("\n\nYou Lost!")
    elif cpoints < hpoints:
        print("\n\nYou Win!")
    else:
        print("\n\nYou Drew!")

while True:
    cpoints = 0
    hpoints = 0
    colour = ["red","blue","yellow","",""]
    
        




































































