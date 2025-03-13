#Ask user to input numbers
numbers = [] #store the input
print("Enter a number, (to stop enter invalid character):")
while True:
    try:
        num = float(input("Number: "))
        
        #if input is unique print "unique" and if input is already in store numbers print "duplicate"
        if num in numbers:
            print ("Duplicate")
        else:
            print("Unique")        
        numbers.append(num)
    except ValueError:
        print("Stoping Program")
        break


#repeat until the user input invalid number to stop