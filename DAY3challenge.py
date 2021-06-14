from tkinter import *
from tkinter import ttk

window = Tk()
#Declaring Window Title
window.title("Registration Screen")
#Declaring Window size
window.geometry('300x300')
#Declaring Window Color
window.configure(background = "purple");
#below four fields are declared
Firstname = Label(window ,text = "First Name").grid(row = 0,column = 0)
MiddleName= Label(window ,text = "Middle Name").grid(row = 1,column = 0)
LastName = Label(window ,text = "Last Name").grid(row = 2,column = 0)
Email = Label(window ,text = "Email Id").grid(row = 3,column = 0)
Mobile = Label(window ,text = "Contact Number").grid(row = 4,column = 0)
AGE= Label(window ,text = "Age").grid(row = 5,column = 0)
counrty= Label(window ,text = "Country").grid(row = 6,column = 0)
city=Label(window ,text = "City").grid(row = 7,column = 0)
state=Label(window ,text = "State").grid(row = 8,column = 0)
pincode=Label(window ,text = "Pincode").grid(row = 9,column = 0)
Qulification=Label(window ,text = "Qulification").grid(row =10,column = 0)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Middlename=Entry(window).grid(row = 1,column = 1)
Lastname1 = Entry(window).grid(row = 2,column = 1)
Email1 = Entry(window).grid(row = 3,column = 1)
Mobile1 = Entry(window).grid(row = 4,column = 1)
AGE= Entry(window).grid(row = 5,column = 1)
country=Entry(window).grid(row = 6,column = 1)
city=Entry(window).grid(row = 7,column = 1)
state=Entry(window).grid(row = 8,column = 1)
pincode=Entry(window).grid(row =9 ,column = 1)
Qulification=Entry(window).grid(row =10,column = 1)
#fubction declaration
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = ttk.Button(window ,text="Submit").grid(row=15,column=0)
window.mainloop()
