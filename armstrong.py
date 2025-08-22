num = int(input("Enter a number: "))
num_digit = len(str(num))
temp = num
sum = 0
while temp>0:
    digit = temp%10
    sum +=digit ** num_digit
    temp //=10
if sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")