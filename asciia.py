s = input("Enter a string: ")
print("The ASCII values of the characters in the string are:")
for char in s:
    print(f"{char}: {ord(char)}")