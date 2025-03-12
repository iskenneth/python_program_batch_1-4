
while True:
    try:
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:")) #Input two numbers
        
        sum = num1  +  num2  #Add the 2 numbers
        print(f"The Sum of {num1} and {num2} are {sum}") #Print result
        break  
        
    except ValueError:
        print("Invalid Character")

