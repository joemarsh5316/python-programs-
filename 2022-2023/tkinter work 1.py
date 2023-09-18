# Import the Tkinter package
from tkinter import *
import time

# Note in Python 3 it is all lowercase from tkinter import *
def background_cycle():
    app.config("#eb4034")
    app.config("#eba534")
    app.config("#ebeb34")
    app.config("#56eb34")
    app.config("#344feb")
    app.config("#b134eb")

def clicked():
    variable = print("i farted")
    background_cycle()
    

# Create a main frame with

# - a title

# - size 200 by 200 pixels

app = Tk()

app.title("GUI exercise 1")

app.geometry('750x500')

# Create the button with
def background_cycle():
    app.config("#eb4034")
    app.config("#eba534")
    app.config("#ebeb34")
    app.config("#56eb34")
    app.config("#344feb")
    app.config("#b134eb")
# - suitable text

# - a command to call when the button is pressed

button1 = Button(app, text="Click Here for funny response",command = clicked())

# Make the button visible at the bottom of the frame button1.pack(side='bottom')
button1.pack(side='bottom')
# Start the application running

app.mainloop()
