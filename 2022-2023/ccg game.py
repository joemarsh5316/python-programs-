pink = "pink"
blue = "blue"
red = "red"
green = "green"
purple = "purple"
score = 0
import random 


def colourChoice(currentScore):
    print("choose between \n 1.pink \n 2.blue \n 3.red \n 4.greed \n 5.purple \n")
    choice = random.randint(1, 5)
    score = currentScore
    choice = str(choice)


    correctanswer = input("what is your guess of the colour chosen\n")

    if correctanswer == choice:
        print("well done! you guessed correct.")
        score = score  + 1
        print(score, "out of ten")
        if score < 10:
            colourChoice(currentScore = score)
        else:
            print("You have won the game")

    elif correctanswer!= choice:
        print("i'm sorry that isn't right")
        print("the correct answer is", choice)
        print (score, "out of ten")
        if score < 10:
            colourChoice(currentScore = score)
        else:
            print("You have won the game")

    
      
colourChoice(currentScore = score)

    
