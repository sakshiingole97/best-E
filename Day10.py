# Python program to create Bankaccount class 
 
class Bank_Account: 

    def __init__(self): 

        self.balance=0

        print("Hello!!!  Most Welcome ") 

  

    def deposit(self): 

        amount=float(input("Enter amount to be Deposited: ")) 

        self.balance += amount 

        print("\n Amount Deposited:",amount) 

  

    def withdraw(self): 

        amount = float(input("Enter amount to be Withdrawn: ")) 

        if self.balance>=amount: 

            self.balance-=amount 

            print("\n You Withdrew:", amount) 

        else: 

            print("\n Insufficient balance  ") 

  

    def display(self): 

        print("\n Net Balance=",self.balance) 

  
# Driver code 

   
# creating an object of class 

s = Bank_Account() 

   
# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 

#To use inheritance in ecommerce concept
#parent class
class Brands:              
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"
    #child class
class Products(Brands):       
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"
    
obj_1 = Products()
print(obj_1.brand_name_1+" is an "+obj_1.prod_1)
print(obj_1.brand_name_2+" is an "+obj_1.prod_2)
print(obj_1.brand_name_3+" is an "+obj_1.prod_3)
