# Get input from user
s = input("Enter a string: ")

# Print the original string
print("Original string:", s)

# Convert the string to uppercase
upper_s = s.upper()
print("Uppercase string:", upper_s)

# Convert the string to lowercase
lower_s = s.lower()
print("Lowercase string:", lower_s)

# Count the number of occurrences of a specific character
c = input("Enter a character to count: ")
count_c = s.count(c)
print("Number of '{0}' characters in string: {1}".format(c, count_c))

# Check if the string starts with a specific prefix
prefix = input("Enter a prefix to check: ")
starts_with_prefix = s.startswith(prefix)
print("String starts with '{0}': {1}".format(prefix, starts_with_prefix))

# Check if the string ends with a specific suffix
suffix = input("Enter a suffix to check: ")
ends_with_suffix = s.endswith(suffix)
print("String ends with '{0}': {1}".format(suffix, ends_with_suffix))

# Split the string into a list of substrings using a delimiter
delimiter = input("Enter a delimiter to split the string: ")
split_s = s.split(delimiter)
print("Split string:", split_s)

print(s.replace('s','z'))
print(s.rfind('t'))
print(s.rindex('t'))
