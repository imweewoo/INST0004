#Exam Grade Average

while True:
    try:
        exams = int(input(f"How many exam grades does each student have: "))
        break
    except ValueError:
        print("This is not a number. Try again.")

studentID = input(f"Enter student ID: ")
print(f"Enter the exam grades.")
total = 0
for i in range(1, len(exams)+1):
    while True:
        try:
            grade = int(input(f"Enter Grade {i}: "))
            break
        except ValueError:
            print("This is not a number. Try again.")

