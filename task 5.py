#Task 1: Calculate Factorial Using a Function 

def Calc_factorial(n):                                #function defination 
    if n == 0 or n == 1:                              #base case
        return 1                                      
    return  Calc_factorial( n - 1) * n                #recursive case

Result = Calc_factorial(int(input("Enter a Number:")))
print(f'The factorial is:{Result}\nProgram ended :) \nThank you')

