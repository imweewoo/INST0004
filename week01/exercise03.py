#Computing balance of an account

#Set initial values
currentBalance = float(20000)
interestRate = 2
expectedBalance = 40000
year = 0

#loop until currentBalance is bigger than expected
while currentBalance < expectedBalance:

    #Calculate added interest in a year
    hold = (currentBalance/100)*interestRate
    currentBalance = hold + currentBalance

    #Increment year
    year += 1

#Print result
print(f"It would take about {year} years for the current account balance to double to the sum of: $40000 or slightly over.")
print(f"The expected balance after {year} years would be: ${round(currentBalance,2)}")