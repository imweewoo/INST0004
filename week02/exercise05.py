#arithmetic computation

def summation(numList, itemNum):
    total = 0
    for i in range(itemNum):
        total = numList[i] + total
    return total

def maximumNumber(numList, itemNum):
    largest = numList[0]
    for i in range(1, itemNum):
        if numList[i] > largest:
            largest = numList[i]
    return largest

def minimumNumber(numList, itemNum):
    smallest = numList[0]
    for i in range(1, itemNum):
        if numList[i] < smallest:
            smallest = numList[i]
    return smallest

def main():
    numList = []

    #item number validation
    while True:
        try:
            itemNum = int(input("Enter the number of items: "))
            break
        except ValueError:
            print("Enter an integer")

    #list of items entry + validation
    for i in range(itemNum):
        while True:
            try:
                num = float(input(f"Enter number in index[{i}]: "))
                break
            except ValueError:
                print("Enter a float")
        numList.append(num)

    #call prior functions
    totalSum = summation(numList, itemNum)
    largest = maximumNumber(numList, itemNum)
    smallest = minimumNumber(numList, itemNum)

    #outputs
    print(f"The total sum is: {round(totalSum,2)}")
    print(f"The maximum number is: {round(largest,2)}")
    print(f"The minimum number is: {round(smallest,2)}")

main()
