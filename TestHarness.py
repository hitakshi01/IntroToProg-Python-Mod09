# ---------------------------------------------------------- #
# Title: Listing 08
# Description: A main module for testing
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ---------------------------------------------------------- #
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO
else:
    raise Exception("This file was not created to be imported")
# Test data module
objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]
for row in lstTable:
    print(row.to_string(), type(row))
# Test processing module
P.FileProcessor.save_data_to_file("PersonData.txt", lstTable)
lstFileData = P.FileProcessor.read_data_from_file("PersonData.txt")
for row in lstFileData:
    p = D.Person(row[0], row[1])
    print(p.to_string().strip(), type(p))

# Test data module
objE1 = D.Employee(1, "Bob", "Smith")
objE2 = D.Employee(2, "Sue", "Jones")
empLstTable = [objE1, objE2]
for row in empLstTable:
    print(row.to_string(), type(row))

# Test processing module
P.FileProcessor.save_data_to_file("EmployeeData.txt", empLstTable)
empLstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
empLstTable.clear()
for line in empLstFileData:
    empLstTable.append(D.Employee(line[0], line[1], line[2].strip()))
for row in empLstTable:
    print(row.to_string(), type(row))

# Test IO classes
IO.EmployeeIO.print_menu_items()
IO.EmployeeIO.print_current_list_items(empLstTable)
print(IO.EmployeeIO.input_employee_data())
print(IO.EmployeeIO.input_menu_options())


