#Ask the user to enter numbers.
numbers = [] #storage
while True:
    try:
        num = float(input("Enter a number (Input invalid character to stop):"))
        numbers.append(num) #Store all valid numbers.
    except ValueError:
        print("Displaying sorted numbers")
        break #Stop when an invalid input is entered.
        


#Sort the numbers in ascending order.
#Display the sorted numbers