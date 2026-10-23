#Exam Grade Average

again = 'Y'
while again.upper() != 'N':
    #Grades + ID input
    while True:
        try:
            exams = int(input(f"How many exam grades does each student have: "))
            break
        except ValueError:
            print("This is not a number. Try again.")

    studentID = input(f"Enter student ID: ")
    print(f"Enter the exam grades.")

    #Get exam grades + totals
    total = 0.0
    grade = 0
    for i in range(1, exams + 1):
        while True:
            try:
                grade = int(input(f"Enter Grade {i}: "))
                break
            except ValueError:
                print("This is not a number. Try again.")
        total = total + grade

    #Output average
    print(f"The student with ID: {studentID} has an average of {round(total/exams,2)}")

    #Loop again?
    again = input(f"Enter exam grades for another student (Y/N)? ")
    while again.upper() != 'Y' and again.upper() != 'N':
                print("Enter y or n")
                again = input("Enter exam grades for another student (Y/N)? ")


