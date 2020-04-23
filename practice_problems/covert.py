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

# write a python program to create a histogram from a given list into a string and return it.
 
    #    [1,3,9,5,8,2]
# @
# @@@
# @@@@@@@@@
# @@@@@
# @@@@@@@
# @@
# @@@@

def histogram(listOfNumbers):
    for num in listOfNumbers:
        print('@'*num)

def histogram1(listOfNumber):
    for num in listOfNumber:
        rv = ''
        for n in range(num):
            rv += '@'
        print(rv)


def diamond(num):
    if(num % 2 == 0): num += 1  # 4 -> 5
    double = num * 2            # 10
    for i in range(1,double):   # 1 - 10
        if(i%2 == 1):
            rv = '*'
            if(i <= num):
                rv *= i
            else:
                j = double - i
                rv *= j

            print(rv.center(num))

def diamond1(num):
    from math import ceil
    if(num % 2 == 0): num += 1   
    mid = ceil(num/2) 
    num1 = num + 1
    for i in range(1,num1):
        blankCount = mid - i
        if(blankCount < 0): blankCount = i - mid
        oddDiff = i - 1
        starCount = i + oddDiff
        if(starCount > num): starCount = i - oddDiff
        rv = ''
        for j in range(blankCount):
            rv += ' '
        for k in range(starCount):
            rv += '*'
        print(rv)

def fizzbuzz():
    for num in range(100):
        result = ''
        if(num % 3 == 0):
            result += 'Fizz'
            
        if(num % 5 == 0):
            result += 'Buzz'
            
        if(result == ''):
            result = num

        print(result)

# fibonacci -> 0 1 1 2 3 5 8 13 21 
def fibonacci(num):
    prev = 0
    next = 1
    print(prev)
    print(next)
    for i in range(num - 2):
        rv = prev + next
        print(rv)
        prev = next
        next = rv
        