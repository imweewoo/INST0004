#Maximum Number Program

def main():

    while True:
        try:
            #Number inputs
            num1 = int(input("Enter your first number: "))
            num2 = int(input("Enter your second number: "))
            num3 = int(input("Enter your third number: "))
            break
        except ValueError:
            print("This is not a number. Try again.")

    #Compare all numbers to find largest
    answer = findMaximum(num1, num2)
    answer = findMaximum(answer, num3)

    print(f"The maximum number is: {answer}")

def findMaximum(num1, num2):

    #Number size comparison
    if num1 > num2:
        return num1
    else:
        return num2

main()
