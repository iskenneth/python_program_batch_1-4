#input two numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))
        
        #Divide the input numbers
        quotient = num1  // num2
        result = int(quotient) #remove the decimals
        print("Quotient without decimal:", result)#print the quotient without the decimal
        break
    except ValueError:
        print("ERRORR!!")

