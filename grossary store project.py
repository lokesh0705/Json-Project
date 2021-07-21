# -*- coding: utf-8 -*-
"""
import mysql.connector
a=mysql.connector.connect(host="localhost",password="",user="root")
print(a)
b=a.cursor()
b.execute("create database grossaryshop")

import mysql.connector
a=mysql.connector.connect(host="localhost",password="",user="root",database="grossaryshop")
print(a)
b=a.cursor()
b.execute("create table products(id char(22), name char(30),price char(22))")



import mysql.connector
a=mysql.connector.connect(host="localhost",password="",user="root",database="grossaryshop")
print(a)
b=a.cursor()
p1 ="emp1"
sql="create table "+p1+"( id int Auto_Increment Primary Key , name char(30),price char(22))"

b.execute(sql)
"""


from tkinter import*
from PIL import Image, ImageTk

def login(): 
    print("lks")
    usr=e1.get()
    pas=e2.get()
    print(usr)
    
    #user=input("enter name")
    import mysql.connector
    a=mysql.connector.connect(
                   host='localhost', user='root',password='',database='user')
    print(a)
    mycursor=a.cursor()
    sql="select *from list where name = %s "
    print(sql)    
    val = (usr,)
    
    mycursor.execute(sql,val)
    
    myresult = mycursor.fetchall()
    ch = False
    for x in myresult:
        if usr in list(x):
             print("\n=================\n")
             ch = True
             print(x)
        else:
            print("\n+++++++++++++++\n")

        myText.set("hello")
  
    if ch:
        print("user found")
        
    else:
        print("not found")
        
        import mysql.connector
        a=mysql.connector.connect(
                   host='localhost', user='root',password='',database='user')
        print(a)
        b=a.cursor()
        sql="insert into list (name,password) values(%s,%s)";
        
        
        val=(usr,pas)
        b.execute(sql,val)
               
        a.commit()



   
master=Tk()

myText=StringVar()
#myText.set("hello")
Label(master,text="user",fg="blue").place(x=10,y=30)
Label(master,text="password",fg="blue").place(x=10,y=50)
result=Label(master,text="",textvariable=myText).place(x=10,y=90)

e1=Entry(master)
e2=Entry(master)

e1.place(x=80,y=20)
e2.place(x=80,y=50)

b=Button(master,text="login",bg="green",command=login).place(x=10,y=120)

mainloop()
