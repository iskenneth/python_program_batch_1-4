#Input two numbers
while True:
    try:
        num1= float(input("Enter a number:"))
        num2= float(input("Enter a number:"))
    except ValueError:
        print("Error")
#Check what is the bigger number (Num1>Num2 or Num2>Num1)
#print the bigger number