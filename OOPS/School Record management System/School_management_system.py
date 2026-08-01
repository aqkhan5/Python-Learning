# School Student Teacher Record management system using object-oriented programming
import json
from abc import ABC, abstractmethod
from pathlib import Path

# Creating database to store the records
database = "school_records.json"
# Creating the copy of database as data
data = {"students":[], "teachers":[]}

# reading the database file if it exists, otherwise creating a new one
def load_database():
    global data
    if Path(database).exists():
        with open(database, "r") as f:
            content = f.read()
            if content:
                data = json.loads(content)
    return data

data = load_database()

# Saving the data to the database file
def save():
    with open(database, "w") as f:
        json.dump(data, f, indent=4)

# Creating an abstract class Person with abstract methods get_roles, register, and show_details. Also, a static method validate_email to check if the email is valid or not.
class Person(ABC):
    @abstractmethod
    def get_roles(self):
        pass

    @staticmethod
    def validate_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_details(self):
        pass

# Creating a class Student that inherits from Person and implements the abstract methods.
class Student(Person):
    def get_roles(self):
        return "Student"
    
    # Method to register a student programmatically
    def register_data(self, name, age, email, roll_no):
        if not Person.validate_email(email):
            return False, "Invalid Email format. Must contain '@' and '.'."
        for i in data["students"]:
            if i["roll_no"] == roll_no:
                return False, f"Roll number {roll_no} already exists."
        data["students"].append({
            "name": name, 
            "age": age, 
            "email": email, 
            "roll_no": roll_no,
            "grades": {}
        })
        save()
        return True, "Student registered successfully."

    # CLI method to register the student
    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        roll_no = int(input("Enter your roll number: "))
        success, msg = self.register_data(name, age, email, roll_no)
        print(msg)

    # Method to add marks programmatically
    def add_marks_data(self, roll_no, subject, marks):
        for s in data["students"]:
            if s["roll_no"] == roll_no:
                s["grades"][subject] = marks
                save()
                return True, f"Marks added successfully for {subject}."
        return False, "Student not found."

    # CLI method to add the marks
    def add_marks(self):
        roll_no = int(input("Enter your roll number: "))
        subject = input("Enter the subject: ")
        marks = int(input("Enter the marks: "))
        success, msg = self.add_marks_data(roll_no, subject, marks)
        print(msg)
        
    def get_student(self, roll_no):
        for s in data["students"]:
            if s["roll_no"] == roll_no:
                return s
        return None

    # CLI method to show the details of the student
    def show_details(self):
        roll_no = int(input("Enter your roll number: "))
        s = self.get_student(roll_no)
        if s:
            grades = s["grades"]
            avg = sum(grades.values())/len(grades) if grades else 0
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Email: {s['email']}")
            print(f"Roll Number: {s['roll_no']}")
            print(f"Grades: {s['grades']}")
            print(f"Average Grade: {avg}")
        else:
            print("Student not found")

# Creating a class Teacher that inherits from Person and implements the abstract methods.
class Teacher(Person):
    def get_roles(self):
        return "Teacher"
    
    # Method to register a teacher programmatically
    def register_data(self, name, age, email, subject, employee_id):
        if not Person.validate_email(email):
            return False, "Invalid Email format. Must contain '@' and '.'."
        for i in data["teachers"]:
            if i["employee_id"] == employee_id:
                return False, f"Employee ID {employee_id} already exists."
            
        data["teachers"].append({
            "name": name, 
            "age": age, 
            "email": email, 
            "subject": subject,
            "employee_id": employee_id,
        })
        save()
        return True, "Teacher registered successfully."

    # CLI method to register the teacher
    def register(self):
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        subject = input("Enter your subject: ")
        employee_id = int(input("Enter your employee ID: "))
        success, msg = self.register_data(name, age, email, subject, employee_id)
        print(msg)

    def get_teacher(self, employee_id):
        for t in data["teachers"]:
            if t["employee_id"] == employee_id:
                return t
        return None

    # CLI method to show the details of the teacher
    def show_details(self):
        employee_id = int(input("Enter your employee ID: "))
        t = self.get_teacher(employee_id)
        if t:
            print(f"Name: {t['name']}")
            print(f"Age: {t['age']}")
            print(f"Email: {t['email']}")
            print(f"Subject: {t['subject']}")
            print(f"Employee ID: {t['employee_id']}")
        else:
            print("Teacher not found")

# Run terminal CLI only when executed directly
if __name__ == "__main__":
    stud = Student()
    teach = Teacher()
    print("Welcome to the School Management System")
    print("1. Register as Student")
    print("2. Register as Teacher")
    print("3. Add Marks (Student only)")
    print("4. Show Student Details")    
    print("5. Show Teacher Details")

    try:
        choice = int(input("Enter Your choice: "))
        if choice == 1:
            stud.register()
        elif choice == 2:
            teach.register()
        elif choice == 3:
            stud.add_marks()
        elif choice == 4:
            stud.show_details()
        elif choice == 5:
            teach.show_details()
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number.")