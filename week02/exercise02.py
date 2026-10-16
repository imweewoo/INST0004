#Volume of a Bottle/Cylinder

#import pi from math library
from math import pi

#Radius entry
while True:
    try:
        r1 = float(input("Enter the first radius (r1): "))
        r2 = float(input("Enter the second radius (r2): "))
        h = float(input("Enter the height (h): "))
        break
    except ValueError:
        print("Please enter a number")

#Calculate bottle volume
volume = pi*(((r1**2 + r1*r2 + r2**2)*h)/3)

#volume output
print(f"The volume of the bottle is: {round(volume,2)} cubic metre")