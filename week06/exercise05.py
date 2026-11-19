#Triangular numebr

class TriangularNumber:
    def generator(self, numb):
        #Base case
        if numb == 1:
            return 1
        else:
            return numb + self.generator(numb -1)

def main():
    while True:
        #number validation + entry
        try:
            num1 = int(input("Enter a positive whole number: "))
            if num1 <= 0:
                raise ValueError(f"Enter a number > 0")
            break
        except ValueError as error:
            if "invalid literal" in str(error):
                print("Enter an integer")
            else: 
                print(error)

    #Create class and output result
    triangle = TriangularNumber()
    print(f"The triangular number of {num1} is {triangle.generator(num1)}")

main()
