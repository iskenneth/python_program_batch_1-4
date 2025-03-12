#Input 10 numbers
sum = 0
for inputs in range(10):
    while True:
        try:
            num = float(input(f"Enter number {inputs + 1}:"))
            
#Add all ten numbers
            sum += num
            break
        
        except ValueError:
            print("ERROOORR!!")           
#print the result
print("Sum of numbers:", sum)
        