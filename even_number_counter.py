#Input 10 numbers
count = 0
even_number = 0
while count < 10:
    try: 
        num = float(input(f"Enter number {count + 1}:"))
        if num % 2 == 0:
            even_number +=1
        count += 1       
    except ValueError:
        print("Error")
#count the numbers
# check each numbers if divisible by 2
#Print how many is even numbers