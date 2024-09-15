#Employee_file = open("employee.txt", "w")
Employee_file = open("employee.txt", "a")
Employee_file.write("\n Mercy - Lawyer", "\n Allan - Human resource")
#for employee in Employee_file.readlines():
    #print(employee)
#print (Employee_file.read())

Employee_file.close()