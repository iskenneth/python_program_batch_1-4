# Input 10 numbers
count = 0
numbers = []
while count < 10:
    try:
        num = float(input(f"Enter number{count +1}:"))
        numbers.append(num) #Store the numbers
        count += 1
    except ValueError:
        print("Error!!")
#Display numbers 
#If numbers have duplicate print only the first one