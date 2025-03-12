#Input two numbers
while True:
    try:
        num1= float(input("Enter a number:"))
        num2= float(input("Enter a number:"))
#Check what is the bigger number (Num1>Num2 or Num2>Num1)
        if num1 > num2: 
              print("Bigger number:", num1)
        elif num2 > num1:
               print("Bigger number:", num2)#print the bigger number
        else:
               print("Both numbers are equal")
        break
    except ValueError:
        print("Error")

