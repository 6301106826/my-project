#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector as sql

connection = sql.connect(
    host="localhost",
    user="root",
    password="Sai@1234"
)

cursor = connection.cursor()
#cursor.execute("CREATE DATABASE Bank1")
connection.commit()


# In[ ]:


import mysql.connector as sql

connection = sql.connect(
    host="localhost",
    user="root",
    password="Sai@1234",
    database="Bank1"
)

cursor = connection.cursor()
#cursor.execute("CREATE TABLE Customers(Account_ID INT PRIMARY KEY, Name VARCHAR(255), Balance VARCHAR(255), Pin INT)")
cursor.execute("select * from Customers")
print(cursor.fetchall())

op = int(input("Press 1 to create an account: "))
if(op==1):
    an = int(input("Enter any new account number: "))
    nm = input("Enter your name: ")
    bal = int(input("Enter Deposit Amount: "))
    pn = int(input("Set up a PIN for transactions: "))
    q1 = "insert into Customers(Account_ID,Name,Balance,Pin) values({},'{}',{},{})".format(an,nm,bal,pn)
    cursor.execute(q1)
    print("Account Created Successfully")
    
else:
    print("Account not created")
    
connection.commit()


# In[ ]:


import mysql.connector as sql

connection = sql.connect(
    host="localhost",
    user="root",
    password="Sai@1234",
    database="Bank1"
)

cursor = connection.cursor()

print("Welcome to ATM\n")
acn = int(input("Please Enter Your Account_ID: "))
q1 = "select * from Customers where Account_ID = {}".format(acn)
cursor.execute(q1)
cursor.fetchone()

if(cursor.rowcount!=0):
    ps = int(input("Enter your PIN: "))
    q2 = "select * from Customers where Pin = {}".format(ps)
    cursor.execute(q2)
    cursor.fetchone()
    
    if(cursor.rowcount!=0):
        print("\n1: Balance Enquiry")
        print("2: Withdrawal")
        print("3: Deposit")
        print("4: PIN Updation\n")
        
        def sb():
            q3 = "select Balance from Customers where Account_ID = {}".format(acn)
            cursor.execute(q3)
            print("Your Current Balance")
            res = cursor.fetchone()
            for i in res:
                print(i)
                
        ch = int(input("Enter Your Choice: "))
        if(ch==1):
            sb()
            
        elif(ch==2):
            amt = int(input("ENTER AMOUNT IN MULTIPLES OF HUNDREDS\n"))
            if amt%100!=0:
                amt = int(input("PLEASE ENTER AMOUNT IN MULTIPLES OF HUNDRED\n"))
            else:
                q4 = "select Balance from Customers where Account_ID = {}".format(acn)
                cursor.execute(q4)
                res = cursor.fetchone()
                for i in res:
                    if amt>int(i):
                        print("Insufficient Funds")
                    else:
                        c = int(i) - amt
                        q5 = "update Customers set Balance={} where Account_ID={}".format(c, acn)
                        cursor.execute(q5)
                        print("Withdrawal Is Successful Collect Money ")
                cb = input("DO YOU WANT TO CHECK BALANCE(Y/N): ")
                if(cb=='Y'):
                        sb()
                        
        elif(ch==3):
            amt = int(input("ENTER AMOUNT IN MULTIPLES OF HUNDREDS\n"))
            if amt%100!=0:
                amt = int(input("PLEASE ENTER AMOUNT IN MULTIPLES OF HUNDRED\n"))
            else:
                q6 = "select Balance from Customers where Account_ID = {}".format(acn)
                cursor.execute(q6)
                res = cursor.fetchone()
                for i in res:
                    da = int(i)+amt;
                    q7 = "update Customers set Balance={} where Account_ID={}".format(da, acn)
                    cursor.execute(q7)
                    print("Deposit Is Successful")
                cb = input("DO YOU WANT TO CHECK BALANCE(Y/N): ")
                if(cb=='Y'):
                    sb()
                    
        elif(ch==4):
            np = int(input("Enter New Pin"))
            q7 = "update Customers set Pin={} where Account_ID={}".format(np, acn)
            cursor.execute(q7)
            print("Pin Change Is Successful")
    else:
        print("PIN Is Wrong")

else:
    print("Account Does Not Exist")
print("\nThank You!!!")

connection.commit()

