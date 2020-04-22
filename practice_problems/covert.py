# fizzbuzz primitive
# for a number input return 'Fizz' if divisible by 3
# 'Buzz' if divisible by 5, 'FizzBuzz' if divisible by 3 and 5
# else return the input

def fizzBuzz(num):
    result = ''
    if(num % 3 == 0):
        result += 'Fizz'
        
    if(num % 5 == 0):
        result += 'Buzz'
        
    if(result == ''):
        result = num
    
    return result

# a = input("Input a Number: ")
# print(a, fizzBuzz(int(a)))

# Write a Python program that accepts an integer (n) 
# and computes the value of n+nn+nnn.

# Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them

def firstLastReverse(firstname, lastname):
    return lastname + ' ' + firstname

# firstname = input('Enter firstname: ')
# lastname = input('Enter lastname: ')
# print(firstLastReverse(firstname, lastname))

def fullNameReverse(name):
    nameArr = name.split(' ')
    firstname = nameArr[0]
    lastname = nameArr[1]
    return lastname + ' ' + firstname

# name = input('Enter name: ')
# print(fullNameReverse(name))

# Write a Python program to accept a filename 
# from the user and print the extension of that.

def getFileExtension(filename):
    ext = filename.split('.')[-1]
    return ext

# filename = input('Enter filename: ')
# print(getFileExtension(filename))

def repeatedSum(number):
    numberString = str(number)
    #n+nn+nnn
    expression = '{n}+{n}{n}+{n}{n}{n}'.format(n=numberString)
    numbers = expression.split('+')
    sum = int(numbers[0]) + int(numbers[1]) + int(numbers[2])
    return expression + ' = ' + str(sum)

# number = input('Enter a number: ')
# number = int(number)
# print(repeatedSum(number))