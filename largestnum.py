numbers = list(map(int,input("Enter numbers separated by space: ").split()))
max_num = numbers[0]
for i in numbers:
    if i>max_num:
        max_num = i
print("The largest number is:", max_num)