import datetime
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import os

from datetime import datetime as dt

def menu():
    global menuv
    menuv = print("""
***** Main Menu ****
1) enter sales records
2) run reports\n""")
    x = int(input(""))
    return x 

def menu2():
    print("""
   **** Reports Dashboard ****
1) Individual Employee Reports\n """)
    x2 = int(input(""))
    return x2

def ind_emp_check(df_r, id, date1, date2):
    df_r = df_r.loc[df.index == id]

    df_r = df_r.T[3:]
    df_r.reset_index(inplace=True)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    date1 = pd.to_datetime(date1, format='%d/%m/%Y')
    date2 = pd.to_datetime(date2, format='%d/%m/%Y')
    mask = (df_r['ID1'] >= date1) & (df_r['ID1'] <= date2)
    df_search = df_r.loc[mask]
    print(df_search)
    print('Total by id = {} is {}'.format(id, sum(df_search[id])))

    plt.bar(df_search['index'], df_search[id])
    plt.xticks(rotation=90)
    plt.show()

    y = menu()
    while y == 1 or y == 2:
        if y == 1:
            try:
                ID = int(input("Enter the Staff ID "))
                if ID not in df.index.values:
                    print('yes')

                date1 = input("Enter Date in dd/mm/yy: ")
                day, month, year = date1.split("/")
                date1 = datetime.date(int(year), int(month), int(day))

                if datetime.datetime.strptime(date1.strftime('%d/%m/%Y'), '%d/%m/%Y') > datetime.datetime.strptime(
                        dt.today().strftime('%d/%m/%Y'), '%d/%m/%Y'):
                    print("Date is in the future")
                else:
                    cost = float(input("Enter the cost : "))
                    df.loc[ID, date1.strftime('%d/%m/%Y')] = cost
                # df.to_csv('test2.csv')
            except:
                print("\n\nError Occurred Please try again\n\n")
                y = menu()

        if y == 2:
            x = menu2()
            if x == 1:
                try:
                    id = int(input("Enter the Employee Id : "))
                    s_date = input("Enter Starting Date in dd/mm/yyyy: ")
                    day, month, year = s_date.split("/")
                    s_date = datetime.date(int(year), int(month), int(day))

                    e_date = input("Enter Date in dd/mm/yyyy: ")
                    day, month, year = e_date.split("/")
                    e_date = datetime.date(int(year), int(month), int(day))

                    s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                    e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                    ind_emp_check(df, id, s_date, e_date)
                except:
                    print("\n\nError Occurred Please try again\n\n")
                    x = menu2()

            else:
                x = menu2()
        else:
            x = menu()
        x = menu()
    root = tk.Tk()
    canvas = tk.Canvas(root, height =1000, width = 1250, bg="#0F3957")
    canvas.pack()
    label = tk.Label(canvas,text = "Main Menu", height = 600, width = 900)
    label.pack()
    text = tk.Text(canvas, height = 5, width = 30)
    text.pack()
    text.insert(tk.END,"""
1) enter sales records
2) run reports\n""")
    root.mainloop()

