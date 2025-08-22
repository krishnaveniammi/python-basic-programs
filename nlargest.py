def n_largest(numbers,n):
    """
    Function to find the n largest numbers in a list.
    
    :param numbers: List of numbers
    :param n: Number of largest elements to find
    :return: List of n largest numbers
    """
    if n <= 0:
        return []
    if n > len(numbers):
        return sorted(numbers, reverse=True)
    
    return sorted(numbers, reverse=True)[:n]
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
n = int(input("Enter the number of largest elements to find: "))
largest_numbers = n_largest(numbers, n)
print(f"The {n} largest numbers are: {largest_numbers}")