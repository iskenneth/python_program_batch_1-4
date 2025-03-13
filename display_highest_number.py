print("to stop the program input invalid character")
#Ask the user to enter numbers continuously.
while True:
    try:
        num = float(input("Enter a number: "))        
    except ValueError:
        print("Stopping the program...")
        break

#Stop when the input is invalid.
#Find and display the highest number entered.