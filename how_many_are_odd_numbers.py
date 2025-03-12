
odd_numbers = 0 # add odd number counter
inputs = 0 #store numbers in list
#Input numbers
while inputs < 10:
    try:
        num = float(input(f"Enter number {inputs + 1}:")) 
        
        #Check each  inputs in the list: if it is a odd number
        if num % 2 != 0:
            odd_numbers += 1
        inputs +=1    #increase the counters
    except VablueError:
        print("ERROR!!")
        
#print how many odd numvers are in the list
print("Count of Odd Numbers:", odd_numbers)    