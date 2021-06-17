#merge two python dictionaries
d1= {"maharashtra":"mumbai","telangana":"hyderabad","tamilnadu":"chennai"}
d2= {"karnataka":"bengaluru","bihar":"patana"}
d3= {**d1,**d2}
print(d3)

# remove the key from the dictionaries
d4={"hello":"23","world":"34","city":"45"}
print(d4)
d5= d4.pop("city")
print(d5)

#list to dictionary
keys=['name','age','job']
value=['john','25','developer']
mydict=dict(zip(keys,value))
print(mydict)

#set lenght
set={"apple","banana","cherry"}
print(len(set))

#intersection of set
a={2,3,4,5}
b={2,5,89}
print(b.intersection(a))
print(a.intersection(b))
