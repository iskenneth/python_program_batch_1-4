#Ask the user to enter numbers.
while True:
    try:
        num = float(input("Enter a number (Input invalid character to stop):"))
    except ValueError:
        print("Displaying sorted numbers")
        break
        
#Store all valid numbers.
#Stop when an invalid input is entered.
#Sort the numbers in ascending order.
#Display the sorted numbers