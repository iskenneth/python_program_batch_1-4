#Range from 1-101
for numbers in range (1,100):
    if numbers % 5 != 0 and numbers % 10 != 0: #check if the numbers is not visible to 10 and 5
        print(numbers, end=" ") # print the numbers if not divisible by 10 and 5
