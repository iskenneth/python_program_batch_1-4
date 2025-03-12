#Input two numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))
    except ValueError:
        print("Invalid Character")
# multiply the input numbers
#print result