#Ask the user to enter numbers.
numbers = [] #storage numbers
while True:
    try:
        num = float(input("Number (input invalid number to stop the program):"))
        numbers.append(num) #Store all valid numbers.
    except ValueError:
        print("Stopping the program...")
        break

#Stop when an invalid input is entered.
#Display the lowest number from the list.