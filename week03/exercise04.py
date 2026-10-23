#Monthly Temperature

#Year entry
while True:
    try:
        year = int(input(f"Enter the year: "))
        break
    except ValueError:
        print("This is not a number. Try again.")

#Loop months 12 times
largest = 0
temp = 0
for i in range(1,13):

    #Month entry
    while True:
        try:
            month = int(input(f"Enter a temperature for month[{i}]: "))
            break
        except ValueError:
            print("This is not a number. Try again.")

    #Find largest month
    if month > largest:
        largest = month
        temp = i

#Output
print(f"Month {temp} has the highest temperature for the year {year}.")