# Anagram number using built-in library
# importing Counter class from collections module
from collections import Counter

s = input("Enter first string: ")
t = input("Enter the second string: " )
print(Counter(s))
print(Counter(t))
print(Counter(s) == Counter(t))
