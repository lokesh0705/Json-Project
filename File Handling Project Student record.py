# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:03:13 2021

@author: Lenovo
"""

#FILE NAME : studentdetail.xls
#file=input("enter the file name")
#f=open(file,"w")
#filename=record.xla

file=input("enter the file name")
while(True):
    print("Press 1.wite 2.append 3.read 4.break")
    ch=int(input("ENTER THE NO."))
    if ch==1:
    
        class students:
            def __init__(s):
             
                name=input("enter the student name")
                s.name=name
                fname=input("enter the fname")
                s.fname=fname
                email=input("enter the email")
                s.email=email
                contact=input("enter the contact")
                s.contact=contact
                
            def child(s):
                f=open(file,"w")
               
                print("child details")
                print(s.name)
                f.write(s.name)
                f.write("\t")
                
                print("father details")
                print(s.fname)
                f.write(s.fname)
                f.write("\t")   
                
                print("enter email")
                print(s.email)
                f.write(s.email)
                f.write("\t") 
                
                print("enter contact no")
                print(s.contact)
                f.write(s.contact)
                f.write("\n") 
                
        d=students()
        d.child()               
                   
            
        
    elif ch==2:        
       
        class students:
            def __init__(s):
                name=input("enter the student name")
                s.name=name
                fname=input("enter the fname")
                s.fname=fname
                email=input("enter the email")
                s.email=email
                contact=input("enter the contact")
                s.contact=contact
                
            def child(s):
                
                f=open(file,"a")
                f.seek(2)
                print("child details")
                print(s.name)
                f.write(s.name)
                f.write("\t") 
                
                print("father details")
                print(s.fname)
                f.write(s.fname)
                f.write("\t")     
                
                print("enter email")
                print(s.email)
                f.write(s.email)
                f.write("\t") 
                
                print("enter contact no")
                print(s.contact)
                f.write(s.contact)
                f.write("\n") 
                
        d=students()
        d.child()                   
                         

    elif ch==3:
         f=open(file,"r")
         print(f.readline ())  
    
    elif ch==4:
        break
   