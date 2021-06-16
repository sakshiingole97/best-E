#Q1 Creating a list.

l=[]
n=int(input("Enter number of elements "))
for i in range(n):
    print("Enter element",i+1," ",end="")
    x=eval(input())
    l.append(x)

print("The list is : ",l)

#Adding a item
x=eval(input("Enter item to be added "))
l.append(x)
#largest number
a=max(l)
print("Largest  number : ",a)
#shortest number
b=min(l)
print("Shortest number : ",b)

#Q2 create tuple and reverse it
print()
z=(1,2,3,5,4)
print("Reverse of the tuple is ")
for j in range(len(z)):
    print(z[len(z)-1-j],end=" ")

#Q3 convert tuple into list
print()
b=(1,2,3,4,5,6,7,8,9,10,11)
print("Tuple is ",b)
m=list(b)
print("converted into list : ",m)
