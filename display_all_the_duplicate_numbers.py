print("Enter 10 numbers")
list_numbers = [] # storage of numbers
#Ask the user to enter 10 numbers.
for number in range (10):
    try:
        num = float(input("Enter number:"))
        list_numbers.append(num) #Store the numbers in a list.
    except ValueError:
        print ("Invalid Character")
        
#Find numbers that appear more than once.
duplicate = set(num for num in list_numbers if list_numbers.count(num) > 1)

#Display only the duplicate numbers (each number is shown once).
