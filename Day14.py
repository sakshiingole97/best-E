#2 simple caluculator using try except blocks

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select the operator")
print(
    "1.additon\n",
    "2.subtraction\n",
    "3.multiplication\n",
    "4.division\n"
    )
print("select among [1,2,3,4] for required operation")
choice = int(input("enter number between [1,2,3,4] only to run operator"))
if choice>4:
    print("enter valid number between [1,2,3,4] only")
    choice = int(input("enter number between [1,2,3,4] only to run operator"))   
    
try:
    first_number=int(input("enter first number"))
    second_number=int(input("enter first number"))

    if choice==1:
        print(first_number,"+",second_number,"=",add(first_number,second_number))
    elif choice==2:
        print(first_number,"-",second_number,"=",sub(first_number,second_number))
    elif choice==3:
        print(first_number,"*",second_number,"=",mul(first_number,second_number))
    elif choice==4:
        print(first_number,"/",second_number,"=",div(first_number,second_number))
    else:
        print("enter number between [1,2,3,4] only")
except ZeroDivisionError as msg:
    print("zero division error please enter number with base 10 only",msg)
except ValueError as msg :
    print("please enter only int value",msg)
else:    
    print("process completed thanks for using our calculator")
          
    









#3
try:
    x=10
    y=ten
    print(x/y)
except NameError:
    print("please enter only integers")
except :
    print("i am default except block")
finally:
    print("you are welcome")
#4
try:
    x=int(input("enter first value"))
    y=int(input("enter second value"))
    print(x/y)
except BaseException as msg:
    print("please enter valid number",msg)
