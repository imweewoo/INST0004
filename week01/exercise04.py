#Number of days in a month

def main():
    month = 100
    year = 100

    #month year loop
    while month != 0 or year != 0:
        month = int(input("Enter the month: "))
        year = int(input("Enter the year: "))

        #Check number of days
        days = dayCalculate(month, year)
        
        #answers or program break
        if month != 0 or year != 0:
            print(f"The number of days in month {month} of year {year} is {days} days.")
        elif month == 0 or year == 0:
            print("Program ended")

#return number of days
def dayCalculate(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 9 or month == 12:
        return 31
    elif month == 4 or month ==6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        is_leap = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
        return 29 if is_leap else 28

main()