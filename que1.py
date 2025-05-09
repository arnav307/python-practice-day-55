# Question:
# Write a Python program that takes a list of strings as input and returns a dictionary.
# The dictionary should have the strings as keys and their lengths as values.
# Implement a helper function `string_length(s)` to calculate the length of a string.

# Example:
# Input: ["apple", "banana", "cherry"]
# Output: {"apple": 5, "banana": 6, "cherry": 6}

def string_length(s):
    dict= {}
    for i in s:
        dict[i] = len(i)
    return dict
# Test the function
print(string_length(["apple", "banana", "cherry","kiwi"]))

