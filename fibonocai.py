def fib(num):
    a ,b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("Fibonacci sequence:")    
print(list(fib(n)))