#Ask the user to Input two numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))

#Proceed to division
        result = num1 / num2
        print(f"Quotient:", result)  #Print the quotient     
        break         
    except ValueError:
        print("ERROR!!!")

