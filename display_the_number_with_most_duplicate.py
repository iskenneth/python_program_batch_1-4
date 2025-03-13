#Ask the user to enter numbers continuously.
print("Good day, this program will stop when you input invalid character")
numbers = [] #input storage
while True:
    try:
        num = float(input("Enter a number: "))
        numbers.appens(num) #store number
    except ValueError:
        print ("Stopping the program....")
        break #Stop when the input is invalid.

#Count how many times each number appears.
if numbers:
    frequent_number = max(set(numbers), key=numbers.count) #find the frequent number
    print("Most common: ", frequent_number)
else:
    print("No valid numbers detected")
