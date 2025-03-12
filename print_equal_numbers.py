#Input two numbers
while True:
    try:
        num1=float(input("Enter a number:"))
        num2=float(input("Enter a number:"))
        
    #Verify if it is equal numbers
        if num1 == num2:
            print(f"{num1} and {num2} are both EQUAL") 
        else:
           print("Numbers are not EQUAL") #print the confirmation
        break
        
    except ValueError:
        print("Invalid Character")
        