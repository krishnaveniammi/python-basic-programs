def is_happy(n):
    seen =set()
    while n !=1 and n not in seen:
        seen.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n ==1
n = int(input("Enter a number: "))
if is_happy(n):
    print(n, "is a happy number")
else:
    print(n, "is not a happy number")    