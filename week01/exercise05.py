#Number of years in months

def main():
    month = 0

    #loop until valid number is entered
    while True:
        try:
            #Entry + check if month is >= 12
            numberOfMonths = int(input("Enter the number of months (over 12): "))
            if numberOfMonths < 12:
                raise ValueError(f"Enter month >= 12")
            break
        except ValueError as error:
            #integer error message
            if "invalid literal" in str(error):
                print("Enter an integer")
            #month size error message
            else:
                print(error)
    #output line + calculation
    print(f"{numberOfMonths} is equal to {numberOfMonths//12} years and {numberOfMonths%12} months.")

main()