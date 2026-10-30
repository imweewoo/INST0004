#Number of Days in Multiple Months

#Library import
from datetime import datetime
import calendar

class CalendarCalculator:

    #Create attributes
    def __init__(self, startDate, months):
        self.startDate = startDate
        self.months = months
        self.endDate = self.addMonths()
        self.startenddays = self.daysBetween()

    def addMonths(self):
        #Find total months with additional month entry
        totalMonths = self.startDate.month -1 + self.months

        #Identify the number of years that need to be added
        year = self.startDate.year + totalMonths//12

        #Find the remaining months
        month = totalMonths % 12 +1

        #Find the last day of the month in a given year
        lastDay = calendar.monthrange(year, month)[1]

        #Find the smallest day between the entered start date, and the end of the month
        day = min(self.startDate.day, lastDay)

        return self.startDate.replace(year=year, month=month, day=day)

    #Return the number of days passed between start and end
    def daysBetween(self):
        return (self.endDate - self.startDate).days

    #Print result
    def OutputData(self):
        print(f"Start Date: {self.startDate.strftime('%d %m %Y')}")
        print(f"End Date: {self.endDate.strftime('%d %m %Y')}")
        print(f"Days: {self.startenddays}")


#Start date entry + validation
while True:
    try:
        dateText = input("Enter start date (dd mm yyyy): ").strip()
        startDate = datetime.strptime(dateText, "%d %m %Y")
        break
    except ValueError:
        print("Invalid date. Please use the format dd mm yyyy")

#Number of months entry + validation
while True:
    try:
        months = int(input("Enter number of months: "))
        if months < 1:
            raise ValueError("Please enter a number of months > 0")
        break
    except ValueError as error:
        #integer error message
        if "invalid literal" in str(error):
            print("Please enter a whole number")
        #too small error message
        else:
            print(error)

#Create object and print results
CalendarObj = CalendarCalculator(startDate, months)
CalendarObj.OutputData()
