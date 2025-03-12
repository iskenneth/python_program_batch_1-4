#Input two numbers
while True:
    try:
        num1=float(input("Enter your first number:"))
        num2=float(input("Enter your second number:"))
    except ValueError:
        print("ERROR!!!")
#Raise the first number to second number
#print result