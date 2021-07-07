#1. Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.
# Using map() and lambda
def listOfTuples(l1, l2):
    return list(map(lambda x, y:(x,y), l1, l2))

l1 = [100, 200, 300, 400, 500]
l2 = ['a' , 'b' , 'c' , 'd' , 'e']
print(listOfTuples(l1, l2))




def merge(l1, l2):
    l1 = [100, 200, 300, 400, 500]
    l2 = ['a' , 'b' , 'c' , 'd' , 'e']
    merged_list = list(zip(l1, l2)) 
    return merged_list

print(merge(l1, l2))

#2. First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.

l1=[1,2,3,4,5,6,7,8]
l2=['a','b','c','d','e','f','g','h']
result =tuple(zip(l1,l2))
print(result)
#3. Using sorted() function, sort the list in ascending order.
l1=[2,8,1,0,4,7,4,3]
l2=sorted(l1)
print(l2)

#4. Write a program using filter function, filter the even nums so that only odd nums are passed to the new list.
def filtereven(nums):
    if nums%2 !=0:
        return True
    else :
        return False

nums =[1,45,16,28,44,76,98,39,12,900]
result=filter(filtereven,nums)
for i in result:
    print(i)
