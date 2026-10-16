#Tourist Direction

def main():
    location = 100
    while location != 0:
        #location validation + input
        try:
            directory()
            location = int(input("Enter the number (0-4): "))
            if location < 0:
                raise ValueError(f"Enter a positive value")
            elif location > 4:
                raise ValueError(f"Enter a value within the range")
        except ValueError as error:
            #integer error message
            if "invalid literal" in str(error):
                print("Enter an integer")
                location = 100
            else:
            #value error message
                print(error)
                location = 100

        #Answer printing
        if location == 1:
            print("***************************************************")
            print("You are at the Harrow-on-The-Hill Station.")
            print("Turn right towards St. Ann's Shopping Centre. ")
            print("***************************************************")
        elif location == 2:
            print("***************************************************")
            print("You are at St. Ann's shopping centre")
            print("Walk towards the exit at the end.")
            print("Turn left towards St. George's Shopping Centre. ")
            print("***************************************************")
        elif location == 3:
            print("***************************************************")
            print("You are at St. George's shopping centre ")
            print("Walk towards the exit on the left.")
            print("Turn right at the exit. ")
            print("Walk straight to Bradstowe House, Headstone Road ahead.")
            print("***************************************************")
        elif location == 4:
            print("***************************************************")
            print("You are at Bradstowe House, Headstone Road. ")
            print("You have reached your destination.")
            print("***************************************************")
        elif location == 0:
            break    
        else:
            print(" ")

#Prints directory information
def directory():
    print("*** Please select an option ***")
    print("0: Exit")
    print("1: Harrow-on-The-Hill Station.")
    print("2: St. Ann's Shopping Centre.")
    print("3: St. George's Shopping Centre")
    print("4: Bradstowe House, Headstone Road.")

main()