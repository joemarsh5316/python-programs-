
    
def palindrome_function():
    i = input("enter number?\n")
    listed= list(i)
    clone = listed.copy()
    clone. reverse()

    if listed == clone:
        print("this is a palindrome. ")
    else:
        print("this is not a palindrome")

while True:
        palindrome_function()
