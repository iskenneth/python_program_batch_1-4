# Input 10 numbers
count = 0
numbers = []
list_numbers = set() # detect input numbers
while count < 10:
    try:
        num = float(input(f"Enter number{count +1}:"))
        numbers.append(num) #Store the numbers
        count += 1
    except ValueError:
        print("Error!!")
        
#Display numbers 
print("List of numbers without repetitions:")
for num in numbers:
    if num not in list_numbers: #If numbers have duplicate print only the first one
        print(num)
        list_numbers.add(num)


