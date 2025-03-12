#Input two numbers
while True:
    try:
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))

#Raise the first number to second number
        result = num1 ** num2
        print("1st number is raised to 2nd number = ", result)  #print result
        break                             
    except ValueError:
        print("ERROR!!!")

