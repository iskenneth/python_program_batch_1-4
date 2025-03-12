#Input 10 numbers
count = 0
even_number = 0
while count < 10:
    try: 
        num = float(input(f"Enter number {count + 1}:"))
        if num % 2 == 0: # check each numbers if divisible by 2
            even_number +=1 #count the numbers
        count += 1     
    except ValueError:
        print("Error")
print("Count of even numbers:", even_number) #Print how many is even numbers       


