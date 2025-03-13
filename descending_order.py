#Ask the user to enter numbers continuously.
while True:
    try:
        num = float(input("Enter a number (to stop enter a letter): "))
    except ValueError:
        print("Stopping program...")
        break #Stop when the input is invalid.

#Sort the numbers from highest to lowest.
#Display the sorted numbers.