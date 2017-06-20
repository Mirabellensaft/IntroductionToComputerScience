# Assume s is a string of lower case characters. Write a program that prints
# the longest substring of s in which the letters occur in alphabetical order.

# For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd',
# then your program should print

# Longest substring in alphabetical order is: abc


s = 'abcbcd'
i = 0
current_str = s[i]
longest_str = s[i]

for i in range(len(s) - 1):
    if s[i] <= s[i + 1]:
        current_str = str(current_str + s[i+1])
        if len(current_str) > len(longest_str):
            longest_str = current_str
    else:
        current_str = s[i+1]
print('Longest substring in alphabetical order is: ' + str(longest_str))
