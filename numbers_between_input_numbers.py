#Ask user to input 2 numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))
    except ValueError:
        print("Error!!!")
#Print numbers in between input numbers