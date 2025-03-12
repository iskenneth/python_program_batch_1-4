#Input to numbers
while True:
    try:
        num1=float(input("Enter your first number:"))
        num2=float(input("Enter your second number:"))
    except ValueError:
        print("Invalid Character")
#Add the input numbers
#Print result