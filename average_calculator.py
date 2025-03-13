#Ask the user to enter numbers continuously.
while True:
    try:
        num = float(input("Enter a number (Input invalid character to stop): "))
    except ValueError:
        print("......")
        break #Stop when the input is invalid.

#Compute the average (sum of numbers divided by count).
#Display the average.