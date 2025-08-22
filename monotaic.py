def is_monotonic(arr):
    """Check if the array is monotonic."""
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False  
    return increasing or decreasing
arr1 = list(map(int, input("Enter numbers separated by space: ").split()))
is_monotonic_result = is_monotonic(arr1)
print("The array is monotonic:", is_monotonic_result)