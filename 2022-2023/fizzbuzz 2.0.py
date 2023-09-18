i = 1
while i <=100:
    if i%3==0:
        print("fizz", end="")
        if i%5==0:
            print("buzz", end="")
    elif i%5==0:
        print("buzz", end="")
    else:
        print(i, end="")
    print()
    i+=1
