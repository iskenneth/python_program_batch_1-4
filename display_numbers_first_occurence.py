# Input 10 numbers
count = 0
while count < 10:
    try:
        num = float(input(f"Enter number{count +1}:"))
        count += 1
    except ValueError:
        print("Error!!")
#Store the numbers
#Display numbers 
#If numbers have duplicate print only the first one