# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# Hitakshi,09.06.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #

if __name__ == "__main__":
    import IOClasses as IO
    import ProcessingClasses as PC
    import DataClasses as DC

else:
    raise Exception("This file is not meant to ran by itself")

# Data -------------------------------------------------------------------- #
strFileName = 'EmployeeData.txt'
lstOfEmployeeObjects = []

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #
try:
    lstFileData = PC.FileProcessor.read_data_from_file(strFileName)
    for line in lstFileData:
        lstOfEmployeeObjects.append(DC.Employee(line[0],line[1], line[2]))
    while True:
        IO.EmployeeIO.print_menu_items()
        userChoice = IO.EmployeeIO.input_menu_options()
        if userChoice == "1":
            IO.EmployeeIO.print_current_list_items(lstOfEmployeeObjects)
        elif userChoice == "2":
            newEmpData = IO.EmployeeIO.input_employee_data()
            lstOfEmployeeObjects.append(newEmpData)
        elif userChoice == "3":
            status= PC.FileProcessor.save_data_to_file(strFileName,lstOfEmployeeObjects)
            if status:
                print("Employee information is saved in the file.")
            else:
                print(" Employee Data is not saved successfully!")
        elif userChoice == '4':
            print("You are exiting from this program!")
            break
        else:
            print("Please select options from [1,2,3]")
except Exception as e:
    print("We ran into technical issue :)")
    raise Exception(e)