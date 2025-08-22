low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))
for i in range(low, high + 1):
    num = i
    num_digit = len(str(num))
    temp = num
    sum = 0
    while temp>0:
        digit = temp%10
        sum +=digit **num_digit
        temp//=10
    if sum == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")