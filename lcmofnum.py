import math 
def lcm(num1,num2):
    """Calculate the Least Common Multiple (LCM) of two numbers."""
    if num1 ==0 or num2 ==0:
        return 0
    else:
        lcm = abs(num1 * num2) // math.gcd(num1, num2)
        return lcm
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = lcm(num1, num2)    
print(f"The LCM of {num1} and {num2} is: {result}")
        