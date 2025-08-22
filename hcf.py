def hcf(num1, num2):
    """Calculate the Highest Common Factor (HCF) of two numbers."""
    if num1 == 0 or num2 == 0:
        return 0
    while num2 !=0:
        num1,num2 = num2, num1 %num2
    return num1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is: {result}")