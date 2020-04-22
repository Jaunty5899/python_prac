# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'i am boring'
age = 1.25

# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting

# Arguments by position
print(name + ' {} {} {}'.format('hello', 1, name ))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world world world this is universe'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone', 1))

# Count
sub = 'h'
print(s.count(sub,2,5))

# Starts with
print(s.startswith('he'))

# Ends with
print(s.endswith('d'))
d='hello world this is alien'
# Split into a list
d = " hello world "
print(d.split(' '))
# s = ' hello world' a = s.split() -> ['hello world']
# s.split(' ') -> ["hello", "world"]
# s.split(' ',1) -> ["hello", "world world world"]
# Find position
print('find ',s.find('world'))
# s = 'hello' a = s.find('l') -> 2

# Is all alphanumeric
a = '/!@#'
print(a.isalnum())
#s = 'abc123' s.isalnum() -> True
#s = 'abc' b.isalnum() -> True
#s = '123' b.isalnum() -> True
#s = '/!@#' b.isalnum() -> False


# Is all alphabetic
print(s.isalpha())
#s = 'abc123' s.isalpha() -> False
#s = 'abc' b.isalpha() -> True
#s = '123' b.isalpha() -> False
#s = '/!@#' b.isalpha() -> False

# Is all numeric
print(s.isnumeric())
#s = 'abc123' s.isnumeric() -> False
#s = 'abc' b.isnumeric() -> False
#s = '123' b.isnumeric() -> True
#s = '/!@#' b.isnumeric() -> False