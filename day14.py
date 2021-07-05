#List down all the error types and check all the errors using a python program for all errors

#Name error

l=12
print(list1)


#Type error

a='abc'
a=a+123  # int + string = invalid type


l=[1,4,3,8,5,9,6,2,7]
for i in range(2,l):
    print(i+1)

#Syntax Error
for i range(1,10):  #for i in range(1,10):   "in" keyword missing
    print(i)

in = 16 # keyword is used as a variable

#index error

list1=[2,3,7,5,1,8,9,5,6]
for i in range(len(list1)):
    print(list1[i+1])


#Module not found error

import modulepsk


#Key error

dict1=dict()
dict1={1:'a',2:'b',3:'c'}
print(dict1[4])



#Import error
from math import xyz


#Value error
int("abc")


#Zero Division Error
print(100/0)

#Design a simple calculator app with try and except for all use cases

def calculate():
    try:
        print('1. "+"')
        print('2. "-"')
        print('3. "*"')
        print('4. "/"')
        print('5. "%"')
        print('6. "**"')
        operation = input("Select an operator:n")
        print("Enter first number:")
        number_1 = int(input())
        print("Enter second number:")
        number_2 = int(input())
        if operation == '+': # To add two numbers
            print(number_1 + number_2)
        elif operation == '-': # To subtract two numbers
            print(number_1 - number_2)
        elif operation == '*': # To multiply two numbers
            print(number_1 * number_2)
        elif operation == '/': # To divide two numbers
            print(number_1 / number_2)
        elif operation == '%': # To remainder two numbers
            print(number_1 % number_2)
        elif operation == '**': # To num1 exponent num2
            print(number_1 ** number_2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)

calculate()

#print one message if the try block raises a NameError and another for other errors
try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    pritn(ve)

'''When try-except scenario is not required?
Python Exceptions are error scenarios that alter the normal execution flow of the program The process of The code inside the else block is executed if there are no exceptions raised.
Try getting an input inside the try catch block
'''
try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
