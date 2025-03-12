#Input two numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))

# multiply the input numbers
        product = num1 * num2 
        print(f"The product of {num1} and num {num2} are {product}") #print result
    except ValueError:
        print("Invalid Character")

