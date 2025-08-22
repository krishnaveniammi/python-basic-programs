low = int(input("Enter a number: "))
high = int(input("Enter another number: "))
for i in range (low,high+1):
    num = i
    if num <= 1:
        continue 
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            break   
    else:
        print(num, "is a prime number") 
        
