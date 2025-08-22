str = input("Enter a string: ")
words = [word.capitalize() for word in  str.split()]
words.sort()
print("Sorted string:", ' '.join(words))