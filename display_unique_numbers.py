#Ask user to input 10 numbers
numbers = [] #store the numbers
count = 0
while count < 10:
    try:
        num = float(input(f"Enter a number{count + 1}:"))
        numbers.append(num)
        count += 1
    except ValueError:
        print("Enter a valid character")

#If number is unique keep it
unique_numbers = [num for num in numbers if numbers.count(num) == 1]

#print unique numbers
print("Numbers without duplicates:")
for num in unique_numbers:
    print(num)