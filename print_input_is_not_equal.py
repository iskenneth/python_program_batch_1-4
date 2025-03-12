#input numbers
while True:
    try:
         num1 = float(input("Enter a number:"))
         num2 = float(input("Enter a number:"))
         
         #check if input numbers is not equal
         if num1 != num2:
             print(f"{num1} and {num2} are NOT EQUAL")                 #print findings
         else:
             print(f"{num1} and {num2} are EQUAL") #print findings
    except ValueError:
         print("ERRORRR!!")

