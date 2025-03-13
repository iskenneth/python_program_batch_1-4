print("Enter 10 numbers")
#Ask the user to enter 10 numbers.
for number in range (10)
    try:
        num = float(input("Enter number:"))
    except ValueError:
        print ("Invalid Character")
#Store the numbers in a list.
#Find numbers that appear more than once.
#Display only the duplicate numbers (each number is shown once).