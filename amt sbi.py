def slip():
    z=int(input("press 1 for slip and 0 for cancel"))
    if z==1:
        print("take the slip")
    else:
        z==0
        print("Thank u for visit")
          
def withdwar():
     l=10000
     for i in range(3):
        a=int(input("enter the amount"))
        if a<10000:
            print("take the cash")
            slip()
            break
        elif a>10000:
            print("enter the value below 10000")
        else:
            break

def genrate_pin():
    t=5
    for i in range(3):
        o=int(input("enter the registered moile no."))
        
        if o == 9462081748:
            r=3
            for i in range(3):
                p=int(input("enter the otp"))
       
                if p==9026:
                    y=int(input("enter new pin"))
                    print("pin updated")
                    break
                    
                elif r>0:
                    r=r-1
                    print("invalid otp")
            
        elif t>0:
                    print("number not registered")
      
    
        
    for i in range(3):
            if p==9026:
                y=int(input("enter new pin"))
                print("pin updated")
                break
            else:
                print("invalid otp")
    
                
                
def deposit():
    b=input("enter the amount")
    print("cash deposited")
    slip()
ch=False
for i in range(3):
    AC_No=input("enter the acc. no")
    pin=input("enter the pin")
    
    if AC_No=="123456" and pin=="123":
        ch=True
        x=4
        for i in range(20):
            print("welcom choose 1 for english , 2 for hindi")
            q=int(input("choose the lanuage"))
            if q==1:
                print("english choosen")
                break
            elif q==2:
                print("hindi choosen")
                break
            else:
                    if x>0:
                        x=x-1
                        print("invalid input")
                    else:
                        break
                   
                
                
        w=int(input("press 1 for withdraw,press 2 for deposit,press 3 for bank statement,press 4 to generate pin"))
        if w==1:
           withdwar()
        elif w==2:
           deposit()
        elif w==3:
            statement()
        elif w==4:
            genrate_pin()
        break
    else :
        print("invalid pin")
        