#Input 10 numbers
sum = 0
for inputs in range(10):
    while True:
        try:
            num = float(input("Enter number {inputs + 1}:"))
        
        except ValueError:
            print("ERROOORR!!")

#Add all ten numbers
#print the result