#Income Tax

tax = 0.0

#Income input
while True:
        try:
            income = float(input(f"Please enter your income: "))
            break
        except ValueError:
                    print("This is not a number. Try again.")

#Conditional outputs based on income size
if income < 12570:
    print(f"Your annual income of £{income} is not taxable.")
    print(f"Your monthly take home salary is £{round(income/12,2)}")
    print(f"Your total net salary is £{income}")
elif income < 50000:
    tax = income*0.2
    print(f"Your annual income of £{income} is taxed at 20% for £{round(tax,2)}")
    print(f"Your monthly take home salary is £{round((income-tax)/12,2)}")
    print(f"Your total net salary is £{income-tax}")
elif income >= 50000 and income < 125140:
    tax = income*0.4
    print(f"Your annual income of £{income} is taxed at 20% for £{round(tax,2)}")
    print(f"Your monthly take home salary is £{round((income-tax)/12,2)}")
    print(f"Your total net salary is £{income-tax}")
elif income > 125140:
    tax = income*0.45
    print(f"Your annual income of £{income} is taxed at 20% for £{round(tax,2)}")
    print(f"Your monthly take home salary is £{round((income-tax)/12,2)}")
    print(f"Your total net salary is £{income-tax}")