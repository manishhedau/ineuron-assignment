# Question - 2
# 2. Write a Python program to reverse a word after accepting the input from the user.
"""
Sample Output:

Input word: ineuron
Output: norueni
"""

input_word = input()
input_word = reversed(input_word)
output = ''

for i in input_word:
    output = output + i

print(output)
