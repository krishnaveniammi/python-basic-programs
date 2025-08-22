def is_pronic(num):
    # Check if num = k*(k+1) for some k
    for k in range(num + 1):
        if k * (k + 1) == num:
            return True
    return False

# Take input from user
n = int(input("Enter a limit: "))

print(f"Pronic numbers up to {n} are:")
for i in range(n + 1):
    if is_pronic(i):
        print(i, end=" ")
