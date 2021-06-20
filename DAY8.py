#merge two dictionaries
dict1={"a":1,"b":2}
dict2={"c":3,"d":4}
dict3=(dict2.update(dict1))
print(dict2)
#sorting and convert list into set
list1 = [4,3,2,1]
list2 =list1[::-1]
set1 = set(list2)
print(set1)
#3) program to list number of items in a dictionary key
names = {3:"a",2:"b",1:"c"}
list3 = dict.keys(names)
print("list of dictionary keys",list3)
sorted_list3 = sorted(list3)
print("sorting the list of dictionary keys", sorted_list3)
#sorting list without using function
names = {3:"a",2:"b",1:"c"}
list4 = dict.keys(names)
list3 = list(list4)
print(list3)

asscending_list = list3[::-1]
print(asscending_list)

#4)
string1 = input("enter a string")
string  = string1[0:10]
print(string)
firstword = string[0:7]
print(firstword)
user_word = input("enter a word")
final_string = string.replace(firstword,user_word)
print(final_string)
#5)

name = input("enter a name")
first_char = name[0]
user_char = input("emter a char")
finalname = name.replace(first_char,user_char)
print(finalname)
#6) repeated items of list
numbers = [1,4,3,2,4,2]
nums = []
for i in numbers:
    if i not in nums:
        nums.append(i)
    else:
        print(i,end=" ")
#7)
elements = [1,2,3]
sum= 0
for i in elements:
    sum = sum+i
print(sum)
user_value = int(input("enter a number"))
dividing_number = sum/user_value
print(dividing_number)

#8)
given_numbers = [1,2,2]
addition = 0
for i in given_numbers:
    addition = addition +i
print("addition",addition)
length = len(given_numbers)
mean = addition/length
print("mean :",mean)

given_numbers.sort()
if length%2==0:
    median1 = given_numbers[length//2]
    median2=given_numbers[length//2-1]
    median = (median1+median2)/2
else:
    median = given_numbers[length//2]
print("median is:",median)
import statistics
mode1=statistics.mode(given_numbers)
print("mode is :",mode1)
#9)
given_string = "India"
update_string = given_string.swapcase()
print(update_string)

#10)
given_int = 11
binary = bin(given_int)
print(binary)
octal = oct(given_int)
print(octal)
