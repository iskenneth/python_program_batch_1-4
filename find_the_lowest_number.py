#Ask the user to enter numbers.
while True:
    try:
        num = float(input("Number (input invalid number to stop the program):"))
    except ValueError:
        print("Stopping the program...")
        break
#Store all valid numbers.
#Stop when an invalid input is entered.
#Display the lowest number from the list.