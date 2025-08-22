num = int(input("Enter a number: "))

if num <= 1:
    print("It's not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("It's not a prime number")
            break
    else:
        print("It's a prime number")
