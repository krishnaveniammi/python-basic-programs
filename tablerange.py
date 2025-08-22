num = int(input("Enter a number: "))
last = int(input("Enter another number: "))
for i in range(num, last + 1):
    print(f"{num} x {i} = {num * i}")