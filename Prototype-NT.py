import copy

class Employee():

    wage = 8
    position ="Server"

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def clone(self):
        return copy.deepcopy(self)

namesOfNewEmployees = ["Joe", "Bob", "Nancy", "Carol"]
newEmployeeObjects = []

employeeTemplate = Employee("Template")

for name in namesOfNewEmployees:
    newEmployee = employeeTemplate.clone()
    newEmployee.name = name
    newEmployeeObjects.append(newEmployee)

for employee in newEmployeeObjects:
    print(employee)



