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
if numbers:
    numbers.sort()
    print ("Ascending order:", numbers)#Display the sorted numbers
else: 
    print("No valid numbers detected")
