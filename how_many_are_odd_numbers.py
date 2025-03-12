
odd_numbers = 0 # add odd number counter
inputs = 0 #store numbers in list
#Input numbers
while inputs < 10:
    try:
        num = float(input(f"Enter number {inputs + 1}:")) 
    except VablueError:
        print("ERROR!!")


#Check each  inputs in the list: if it is a odd number increase the counter
#print how many odd numvers are in the list
     