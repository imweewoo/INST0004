#Volume of a sphere

#import pi from math library
from math import pi

#Radius entry
while True:
    try:
        radius = float(input("Enter the radius of a sphere: "))
        break
    except ValueError:
        print("Please enter a number")

#Calculate volume
volume = (4/3)*(pi)*(radius**3)

#volume output
print(f"The volume of the sphere is: {round(volume,2)}")
