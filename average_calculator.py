#Ask the user to enter numbers continuously.
numbers = [ ]
while True:
    try:
        num = float(input("Enter a number (Input invalid character to stop): "))
        numbers.append(num)
    except ValueError:
        print("......")
        break #Stop when the input is invalid.

#Compute the average (sum of numbers divided by count).
#Display the average.