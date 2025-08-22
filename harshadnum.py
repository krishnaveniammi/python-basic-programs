def harshad(num):
    """
    Check if a number is a Harshad number.
    A Harshad number is an integer that is divisible by the sum of its digits.
    """
    digits_sum = sum(int(digit) for digit in str(num))
    return num%digits_sum == 0
num = int(input("Enter a number: "))
if harshad(num):
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number") 