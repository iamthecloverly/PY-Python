# create a list of integers
numbers = list(map(int,input().split()))

# print the entire list
print(numbers)

# access individual elements by index
print(numbers[0]) # prints 1
print(numbers[2]) # prints 3

# change the value of an element
numbers[0] = 0
print(numbers) # prints [0, 2, 3, 4, 5]

# add an element to the end of the list
numbers.append(6)
print(numbers) # prints [0, 2, 3, 4, 5, 6]

# insert an element at a specific index
numbers.insert(1, 1)
print(numbers) # prints [0, 1, 2, 3, 4, 5, 6]

# remove an element by value
numbers.remove(3)
print(numbers) # prints [0, 1, 2, 4, 5, 6]

# remove an element by index
del numbers[0]
print(numbers) # prints [1, 2, 4, 5, 6]

# get the length of the list
print(len(numbers)) # prints 5

# check if an element is in the list
print(4 in numbers) # prints True
print(7 in numbers) # prints False
