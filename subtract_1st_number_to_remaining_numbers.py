#Input 10 numbers
while True: 
    try:
        numbers : [] #store numbers
        for number in range(10):
            num = float(input(f"Enter {number + 1}:"))
            numbers.append(num) #Get the first number
        
        # Subtract the first number to the rest
        result = numbers[0] - sum(numbers[1:])
        print ("Diffirence: ", result) # Print result
        break
    except ValueError:
        print("ERROR 404!!")    


