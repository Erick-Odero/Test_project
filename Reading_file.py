Employee_file = open("employee.txt", "r")
for employee in Employee_file.readlines():
    print(employee)
#print (Employee_file.read())

Employee_file.close()