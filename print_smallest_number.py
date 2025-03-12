#Input two numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))

#compare which is the smallest number
        if num1 < num2:
            print(f"{num1} is smaller") #print the smallest number
        elif num2 < num1:
            print(f"{num2} is smaller") #print the smallest number
        else:
            print("Numbers are equal")
        break               
    except ValueError:
        print("ERRORRR!!")

