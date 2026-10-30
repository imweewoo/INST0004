#Employee Record and Incoem Increment

class Employee:
    def __init__(self, name, job=None, pay=0.0):
        self.name = name
        self.job = job
        self.pay = pay

    #Return last name
    def lastName(self):
        return self.name.split()[-1]

    #Return pay with increase
    def payIncrement(self, percent):
        return round((self.pay * (100+percent)/100), 2)

#Create objects
danny = Employee("Danny Onah")
elaine = Employee("Elaine Jones", "Lecturer", 39000)

#Display last name
print(f"{danny.lastName()} {elaine.lastName()}")

#Display surname, job, pay of elaine
print(f"Surname: {elaine.lastName()} Job Title: {elaine.job} Pay: {elaine.pay}")

#Display pay increment
print(f"Pay increased by 10 percent is: £{elaine.payIncrement(10)}")