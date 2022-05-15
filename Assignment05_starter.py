# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What): Maria Lee, 15-5-22
# RRoot,1.1.2030,Created started script
# <Maria Lee>,<15-5-22>, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
objFile = None
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
dicRow = {"task": "dishes", "priority": "mid"}
objFile = open(strFile, "w")
objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")
lstTable = [dicRow]
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of IFIIchoices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("your current data is")
        for row in lstTable:
            print(row)
        continue
    # Step 4 - Add a new tasks to the list/Table
    elif (strChoice.strip() == '2'):
        # objFile = open(strFile, "w")
        newtask = input("task: ")
        newpriority = input("priorities (high, mid, low): ")
        dicRow = {"task": newtask, "priority": newpriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a item from the list/Table
    elif (strChoice.strip() == '3'):
        remove = input("task to remove: ")
        remove = remove.lower()
        for row in lstTable:
            if (row["task"] == remove):
                lstTable.remove(row)
                print("task removed")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["task"] + ", " + row["priority"] + '\n')
        objFile.close()
        print("data save to file")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("exiting programme")
        break  # and Exit the program


