#fizzbuzz primitive
#for a number input return 'Fizz' if divisible by 3
#'Buzz' if divisible by 5, 'FizzBuzz' if divisible by 3 and 5
#else return the input

# a,flag = input("Input a Number: "),''
# a = int(a)
# if (a%3==0):
#     flag+='Fizz'

# if (a%5==0):
#     flag+="Buzz"

# if(flag==''):
#     print(a)
# else:
#     print(flag)  
    
# if (flag==0):
#     print('fizz')
# elif (flag==-1):
#     print('Buzz')
# elif (flag==2):
#     print('FizzBuzz')
# else:
#     print(a)    



# if (a%3==0): 
#     if(a%5==0):
#         print('fizzbuzz')
#     else:
#         print('fizz')    
# elif(a%5==0):
#     print('Buzz')
# else:
#     print(a)    
# # ---------------------------------

# Write a Python program which accepts the user's first and last name 
# and print them in reverse order with a space between them
# a = input("Input full name: ").split(' ')
# a.reverse()
# print(a[0],a[1])

# Write a Python program to accept a filename 
# from the user and print the extension of that.
# a = input("Input file name: ")
# index = a.find('.')
# print(a[index+1:len(a)])

# Write a Python program that accepts an integer (n) 
# and computes the value of n+nn+nnn.
# eg input = 5, result = 5 + 55 + 555 = 615
# input = 12, 12 + 1212 + 121212
# a = input("Input number: ")
# sum = int(a) + int(a*2) + int(a*3)
# # print('sum =',a,'+',a*2,'+',a*3,'=',sum)

# # write a python program to create a histogram from a given list into a string and return it.
 
#     #    [1,3,9,5,8,2]
# # @
# # @@@
# # @@@@@@@@@
# # @@@@@
# # @@@@@@@
# # @@
# # @@@@

# b = [3,8,1,5,10,7,2]

# for i in b:
#     a=''
#     # print(a*i)
#     for j in range(i):
#         a+='*'
#     print(a)  
#     # print('\n')

# def diamond(b):
#     c = b.copy()
#     c.sort()
#     for i in b:
#         a=''
#         # print(a*i)
#         for j in range(i):
#             a+='*'
#         print(a.center(c[-1]))
#         # # c-=1

# diamond([1,3,5,7,9,11,13,15,13,11,9,7,5,3,1])

def fizzbuzz():
    for i in range(1,101):
        if(i%3==0 and i%5==0):
            print('FizzBuzz')
        elif(i%5==0):
            print('Buzz')   
        elif(i%3==0):
            print('Fizz')
        else:
            print(i)    

fizzbuzz()      

# fibonacci -> 0 1 1 2 3 5 8 13 21 

def fibon(input):
    a=[0,1]
    if input!=2:
        for i in range(input-2):
            a.append(a[i]+a[i+1])    
    print(a)

fibon(3)

# 4! -> 1.2.3.4 = 24

def fact(input):
    a=input
    input-=1
    if a==1:
        return 1
    else:    
        return a*fact(input)
print(fact(4))    
# a, b = [int(i) for i in input().split()]

def srh():
    s = input('Enter alphanumeric name: ')
    b = ''
    a = ['0','1','2','3','4','5','6','7','8','9']
    for i in s:
        isNumber = i in a       # input = 'J2aun7ty'
        if not isNumber:
                b+=i               # if(truthyValue)
                                # if(not isNumber)
                      
                                    #if(isNumber == True)  is same as if(isNumber)
                                    # i = 'J'
                                    # flag = 0, flag =1,2
                                    #if(not flag):  code here runs when flag is 0

            
        
    print(b)   

srh()


def srh1():
        s = input('Enter alphanumeric name: ')
        b = ''
        a = ['0','1','2','3','4','5','6','7','8','9']
        for i in s:
            # input = 'J2aun7ty'
            # i = '2'
            isChar = 1
            for j in a:
                # j = '0'
                if i == j: # 'J' == '0'   
                    isChar = 0;
                    break;  
  
            if isChar:
                b+=i
            
                        
                    # b = 'JJJJJJJJ'
        print(b)   
srh1()