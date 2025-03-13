#Ask user to input numbers
numbers = [] #store the input
print("Enter a number, (to stop enter invalid character):")
while True:
    try:
        num = float(input("Number: "))
    except ValueError:
        print("Stoping Program")
        break

#if input is unique print "unique" and if input is already in store numbers print "duplicate"
#repeat until the user input invalid number to stop