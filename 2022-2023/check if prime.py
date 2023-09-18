input("what is your number\n")
def checkifprime (number):
    for x in range(2, number):
        if(number%x==0):
            print("this number isnt prime")
        elif(number%x==1):
            print("this number is prime")
