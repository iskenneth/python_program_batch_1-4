#Ask user to input 10 numbers
while count < 10:
    try:
        num = float(input(f"Enter a number{count+1}:""))
    except ValueError:
        print("Enter a valid character")
#store the numbers
#If number is unique keep it
#print unique numbers