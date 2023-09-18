import tkinter as tk
import os

root = tk.Tk() 

def back():    
    pack_forget(label)
    pack_forget(label2)
    pack_forget(passentry)
    pack_forget(button1)
    pack_forget(button2)
def login():
    global nameput
    global passput
    nameput = tk.StringVar()
    passput = tk.StringVar()
    label = tk.Label(frame,text = "Enter Username", bg = "grey", fg = "black").pack()
    nameentry = tk.Entry(frame,textvariable = nameput).pack()
    label2 = tk.Label(frame,text = "Enter Password", bg = "grey", fg = "black").pack()
    passentry = tk.Entry(frame, textvariable = passput,show = "*").pack()
    button1 = tk.Button(frame, text = "Login", bg = "grey", fg= "black", command = check).pack()
    button2 = tk.Button(frame,text = "Back", bg= "grey", fg = "black", command = back).pack()

    root.mainloop()

def check():
    if nameput and passput == "joe" and "marshy123":
        menu()
    elif nameput and passput != "joe" and "marshy123":
        tk.Label(frame, text= "that is incorrect try again")


def home():
    root
    canvas = tk.Canvas(root, height = 700, width = 700, bg = "#152238")
    canvas.pack()
    global frame
    frame = tk.Frame(root, bg="#203354")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    button = tk.Button(frame, text=" staff login", padx=10, pady=5, bg="grey", fg="black", command = login).pack()
    
    root.mainloop()
    
home()
