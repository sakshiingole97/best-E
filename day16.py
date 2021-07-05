#1. Create a lambda function that multiplies argument x with argument 
r = lambda x, y : x * y
print(r(5,2))

#2. Write a Python program to create Fibonacci series to n using Lambda

from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])

print(fib(10))

#3. Write a Python program that multiply each number of given list with a given number

num = [1,3,4,7,2,5]
n = 2
print("Given list: ", num)
print("Number to be multiplied: ", n)
filter_num=list(map(lambda number:number*n,num))
print("Final list :")
print(' '.join(map(str,filter_num)))


#4. Write a Python program to find numbers divisible by 9 from a list of numbers

l=[1,33,54,32,12,6,44,27,81,65,43,90]
print("List1:")
print(l)
m=list(map(lambda j:j%9==0,l))
print("If numbers divisible by 9:")
print(' '.join(map(str,m)))
m=list(filter(lambda j:j%9==0,l))
print("Numbers:")
print(' '.join(map(str,m)))

#5. Write a Python program to count the even numbers in a given list of integers

list_1=[1,4,6,3,8,6,4,3,1,5,9]
print("List : ")
print(list_1)
list_2=list(filter(lambda j:j%2==0,list_1))
print("Even numbers : ")
print(len(list_2))
