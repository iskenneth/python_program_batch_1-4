#Ask user to input 2 numbers
while True:
    try:
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter a number:"))
        
        if num1 > num2:
            num1, num2 == num2, num1
        start = int(num1) + 1
        end = int(num2)
        print ("Numbers between: ", end = " ")
        for num in range (start, end):
            print (num, end =" ") #Print numbers in between input numbers
        break
    except ValueError:
        print("Error!!!")
