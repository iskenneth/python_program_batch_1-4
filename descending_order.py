#Ask the user to enter numbers continuously.
inputs = [ ] #input storage
while True:
    try:
        num = float(input("Enter a number (to stop enter a letter): "))
        inputs.append(num) #store inputs
    except ValueError:
        print("Stopping program...")
        break #Stop when the input is invalid.

#Sort the numbers from highest to lowest.
if inputs:
    inputs.sort(reverse = True)
    print("Descending order: ", inputs) #Display the sorted numbers.
else:
    print("There is no valid number detected")
    
