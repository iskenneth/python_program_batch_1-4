#Ask the user to Input two numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))

    except ValueError:
        print("ERROR!!!")
#Proceed to division
#Print the quotient