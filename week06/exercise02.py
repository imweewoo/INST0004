#factorial number

#Factorial calculation function
def fact(numb):
    if numb > 1:
        return numb*fact(numb-1)
    return 1 

def main():

    while True:
    #Number validation
        try:
            num1 = int(input("Enter an integert to calculate the factorial of: "))
            if num1 <= 0:
                raise ValueError(f"Enter a positive number")
            break
        except ValueError as error:
            if "invalid literal" in str(error):
                print("Enter an integer")
            else: 
                print(error)

    #Output results
    factorial = fact(num1)
    print(f"The factorial of {num1}! is: {factorial}")

main()