


def fibbonacci_sequence():
    
    nterms = int(input("how many terms? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <=0:
        print("please enter a positive number")
        while True:
            fibbonacci_sequence()
    elif nterms == 1:
        print("Fibbonacci sequence upto", nterms, ":")
        print(n1)
        while True:
            fibbonacci_sequence()
    else:
        print("fibbonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1

    import turtle
    a = turtle.Turtle()

    for i in range(count):
        a.forward(30+i)
        a.left(40 - i/1.5)

    turtle.done


fibbonacci_sequence()

while True:
        fibbonacci_sequence()    
    
