#Lifts Program - Apartments & Buildings

#Import libraries
import random

#Find smallest floor and lift
def minimumFloor(liftFloors):
    minLift = 1
    minFloor = liftFloors[0]
    for i in range(1, len(liftFloors)):
        if liftFloors[i] < minFloor:
            minFloor = liftFloors[i]
            minLift = i + 1
    return minLift, minFloor

#Find largest floor and lift
def maximumFloor(liftFloors):
    maxLift = 1
    maxFloor = liftFloors[0]
    for i in range(1, len(liftFloors)):
        if liftFloors[i] > maxFloor:
            maxFloor = liftFloors[i]
            maxLift = i + 1
    return maxLift, maxFloor

def main():
    callAgain = 'y'
    liftFloors = []
    while callAgain != 'n':

        #validation + lift numeber input + target floor input
        liftNumber = int(input("Enter the number of lifts: "))
        while liftNumber < 2:
            print("There must be at least 2 lifts")
            liftNumber = int(input("Enter the number of lifts: "))

        targetFloor = int(input("Enter the floor you are on (0-9) "))
        while targetFloor < 0 or targetFloor > 9:
            print("Enter floor numbers within range")
            targetFloor = int(input("Enter the floor you are on (0-9) "))

        #Randomly assign lift floors
        for i in range(liftNumber):
            liftFloors.append(random.randrange(0,10))
            print(f"Lift {i+1} is on floor {liftFloors[i]}")

        print(f"Lift closest to user on floor {targetFloor} is called.")

        #Find min max floors + lift numbers
        minLift, minFloor = minimumFloor(liftFloors)
        maxLift, maxFloor = maximumFloor(liftFloors)

        # Decide which lift to call
        if minFloor == maxFloor:
            chosenLift = minLift
            print(f"All lifts are on floor {minFloor}, so lift {chosenLift} is chosen.")
        elif targetFloor <= minFloor:
            chosenLift = minLift
        elif targetFloor >= maxFloor:
            chosenLift = maxLift
        else:
            chosenLift = 1
            smallestGap = abs(targetFloor - liftFloors[0])
            for i in range(1, len(liftFloors)):
                gap = abs(targetFloor - liftFloors[i])
                if gap < smallestGap:                    # strict < keeps the smaller lift number on a tie
                    smallestGap = gap
                    chosenLift = i + 1

        # Display the result
        chosenFloor = liftFloors[chosenLift - 1]
        if targetFloor == chosenFloor:
            print(f"Lift {chosenLift} is already on your floor ({targetFloor}) and is called.")
        elif targetFloor > chosenFloor:
            print(f"Lift in higher floor {chosenLift} is called")
        else:
            print(f"Lift in lower floor {chosenLift} is called")

        #Reloop
        callAgain = input("Call another lift? (y/n) ")
        liftFloors = []
        while callAgain != 'y' and callAgain != 'n':
            print("Enter y or n")
            callAgain = input("Call another lift? (y/n)")

main()