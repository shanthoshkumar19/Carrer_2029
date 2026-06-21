class Student:

    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.dept)


s1 = Student("Shanthosh", 18, "CSE")

s1.display()