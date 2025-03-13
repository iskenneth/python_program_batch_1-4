#Ask the user to enter numbers continuously.
print("Good day, this program will stop when you input invalid character")
while True:
    try:
        num = float(input("Enter a number: "))
    except ValueError:
        print ("Stopping the program....")
        break
#Stop when the input is invalid.
#Count how many times each number appears.
#Find and display the number that appears the most.