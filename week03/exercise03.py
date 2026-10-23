#Grade Computation

#Initialise variables
grade = 0
count = 0
total = 0
fail = 0
passing = 0
smallest = 100
largest = 0

#Loop until -1
while grade != -1:

    #Grade entry
    while True:
            try:
                grade = int(input(f"Enter a grade or -1 to finish: "))
                break
            except ValueError:
                print("This is not a number. Try again.")

    #Find passing and failing grade + add to total and count
    if grade < 40 and grade > -1:
        fail += 1
        count += 1
        total = total + grade
    elif grade >= 40 and grade <= 100:
        passing += 1
        count += 1
        total = total + grade

    #Find max and min
    if grade < smallest and grade != -1:
        smallest = grade
    elif grade > largest:
        largest = grade

#Output grade statistics
print(f"The average grade is {round(total/count,2)}")
print(f"Number of failing grades is: {fail}")
print(f"Number of passing grades is: {passing}")
print(f"The maximum grade is: {largest}")
print(f"The minimum grade is: {smallest}")

#Pass or fail comparison output
if passing > fail:
    print("Congratulations! Proceed to the next level. ")
elif passing < fail: 
    print("You will need to perform better")
elif passing == fail:
    print("You are in-between passing and failing!\nYou would need to study more!")