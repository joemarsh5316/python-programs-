import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
def barh():
    x = ['A','B','C','D','E']
    y = [10,5,8,6,12]
    plt.barh(x, y)
    plt.show()
def heatmap():
    import numpy as np
    import seaborn as sns
    data = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,12,15,16]])
    ax = sns.heatmap(data, linewidth = 0.5, cmap='coolwarm')
    plt.show()
def dual_axis():
    x = [1,2,3,4,5]
    plt.xlabel("x axis")
    y1 = [2,4,5,6,10]
    y2 = [5,3,1,7,2]
    plt.ylabel("y axis")
    plt.plot(x, y1, y2)
    plt.show()
def pie():
    my_labels = ['Apples', 'Bananas', 'Cherries', 'dates']
    data = [30,25,20,10]
    plt.pie(data, labels = my_labels)
    plt.show()
def menu():
    print("""******************************************************************************
                 _         _       _   _ _ _                                  
                | |       | |     | | | (_) |                                 
 _ __ ___   __ _| |_ _ __ | | ___ | |_| |_| |__    _ __ ___   ___ _ __  _   _ 
| '_ ` _ \ / _` | __| '_ \| |/ _ \| __| | | '_ \  | '_ ` _ \ / _ \ '_ \| | | |
| | | | | | (_| | |_| |_) | | (_) | |_| | | |_) | | | | | | |  __/ | | | |_| |
|_| |_| |_|\__,_|\__| .__/|_|\___/ \__|_|_|_.__/  |_| |_| |_|\___|_| |_|\__,_|
                    | |                                                       
                    |_|
******************************************************************************""")
    print("""******************************************************************************
| 1) barh                                                                    |
| 2) heatmap                                                                 |
| 3) dual axis                                                               |
| 4) pie                                                                     |
| 5) stacked bar                                                             |
| 6) scatter plot                                                            |
|****************************************************************************|""")
    
    choice = input("what chart would you like to see?\n")
    if choice == "1":
        barh()
        while True:
            menu()
    elif choice == "2":
        heatmap()
        while True:
            menu()
    elif choice == "3":
        dual_axis()
        while True:
            menu()
    elif choice == "4":
        pie()
        while True:
            menu()
    else:
        print("thats not a valid choice!")
        while True:
            menu()
menu()
