#Creating and writing in a File
f =open(r"30_days_30_hours_operations.txt","w+")
f.write("Hey all!! Finally, I have completed 10 days of Code successfully")
f.close()

#Appending in a created file
f1 =open(r"30_days_30_hours_operations.txt","a+") 
f1.writelines(": sakshi")
#Reading the content in a file
f1 =open(r"30_days_30_hours_operations.txt","r") 
print(f1.read())

#Closing the file object
f1.close()
