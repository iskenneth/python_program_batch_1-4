#Input numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))
        
        # Perform modulus division on num1 to num 2
        result = num1 % num2
        print("Remainder:", result) # Print the result
        break
    except ValueError:
        print("INVALID CHARACTER")

