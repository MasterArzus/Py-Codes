def displayCount():
    print("Employee number: " + str(Employee.empCount))


class Employee(object):
    empCount = 0

    def __init__(self, name, salary):
        Employee.empCount += 1
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("Name: " + self.name)
        print("Salary: " + str(self.salary))


# 创建Employee类的第一个对象
emp1 = Employee("Tim", 4000)
# 输出Employee类实例化的对象总数
displayCount()
# 输出Tim的信息
emp1.displayEmployee()

# 创建Employee类的第二个对象
emp2 = Employee("Bob", 4640)
# 输出Employee类实例化的对象总数
displayCount()
# 输出Bob的信息
emp2.displayEmployee()
