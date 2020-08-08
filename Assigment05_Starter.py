# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <DAVID JAMIESON>,<8/8/2020>, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strItem = () # TO capture user input of a new item
strValue = () # To capture user input of a new item's value

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)


objFile = open("C:\_PythonClass\Assignment05\ToDoList.txt", "r")
for row in objFile:
    item, value = row.split(",")
    dicRow = {"Item": item.strip(), "Value": value.strip()}
    lstTable.append(dicRow)

objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options:
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
        print("Here is the current data in your table:")
        print(lstTable)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strItem = str(input("Please enter an item:"))
        strValue = str(input("Please enter a value for the item: "))
        dicRow = {"Item": strItem.strip(), "Value": strValue.strip()}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItem = input("Item to Remove: ")
        for row in lstTable: #this prints on every line, look into fixing
                if row["Item"].lower() == strItem.lower():
                    lstTable.remove(row)
                    print(strItem, " has been removed from the table")
                else:
                    print(strItem, " was not found in table")

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("C:\_PythonClass\Assignment05\ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Item"]) + ',' + str(row["Value"] + '\n'))
        objFile.close()
        print("Table saved to file, TodoList.txt")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Program has been exited - thank you!')
        break  # and Exit the program

    else:
        print("Please enter a number from [1 to 5]. Your input was not accepted.")
