# Understanding the oop concept of class and object

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def study(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no} is preparing for the exam.")

# Creating an object of the Student class
student1 = Student("Abdul Qadeer", "COMPF22BSR47")
student2 = Student("Ali", "COMPF22BSR99")

# Calling the study method on the object
print(student1.name, student1.roll_no)
print(student2.name, student2.roll_no)

# performing actions on the object
student1.study()
student2.study()


# Method with parameters and return type
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

