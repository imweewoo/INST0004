#Student Record

class Student:
    #Create attributes
    def __init__(self, id, name, department):
        self.id = id
        self.name = name
        self.department = department

    #Print details
    def student_detail(self):
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")
        print(f"Student Department: {self.department}")

#ID only 8 digits entry and validation
while True:
    try:
        studentID = input("Enter studentID: ").strip()
        if not studentID.isdigit() or len(studentID) != 8:
            raise ValueError("Student ID must be 8 digits, e.g. 12393049")
        break
    except ValueError as error:
        print(error)

#Name only characters, spaces, - , '
while True:
    try:
        studentName = input("Enter studentName: ").strip()
        if not studentName.replace(" ", "").replace("-", "").replace("'", "").isalpha():
            raise ValueError("Name must only contain letters, spaces, hyphens or apostrophes")
        break
    except ValueError as error:
        print(error)

#Department only spaces or characters
while True:
    try:
        studentDept = input("Enter studentDept: ").strip()
        if not studentDept.replace(" ", "").isalpha():
            raise ValueError("Department must only contain letters and spaces")
        break
    except ValueError as error:
        print(error)

studentObj = Student(studentID, studentName, studentDept)
studentObj.student_detail()