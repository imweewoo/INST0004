#Number of years in months

def main():
    month = 0

    while True:
        try:
            numberOfMonths = int(input("Enter the number of months (over 12): "))
            break
        except ValueError:
            print("Enter an integer.")

    print(f"{numberOfMonths} is equal to {numberOfMonths//12} years and {numberOfMonths%12} months.")

main()