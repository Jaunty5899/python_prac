# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Grapes')

# Insert into position
# print('before insert ', fruits)
fruits.insert(2, 'Strawberries')
# print('after insert ', fruits)

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
# print('before pop at index 2 ', fruits)
a = fruits.pop(2)
# print('a = ', a)
# print('after pop at index 2 ', fruits)

# Reverse list
# print('before reverse ', fruits)
fruits.reverse()
# print('after reverse ', fruits)

# Sort list
fruits.sort()
alphabets = ["c","a","d","z"]
alphabets.sort()
numbers = ['10','1','2','22','3','9','0','abc']
numbers.sort()
print('sorted -> ',numbers)


# Reverse sort
fruits.sort(reverse=True)

print(fruits)
