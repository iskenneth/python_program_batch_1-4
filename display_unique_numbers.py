#Ask user to input 10 numbers
numbers = [] #store the numbers
count = 0
while count < 10:
    try:
        num = float(input(f"Enter a number{count + 1}:"))
        numbers.append(num)
        count += 1
    except ValueError:
        print("Enter a valid character")

#If number is unique keep it
#print unique numbers