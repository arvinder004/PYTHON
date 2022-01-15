#basic calculator

def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def multiply(a,b):
    return(a*b)

def divide(a,b):
    return(a/b)

def pow(a,b):
    return(a**b)

def fact(a):
    b=1
    for i in range(1,a+1):
        b*=i
    return(b)


while True:
    print("SELECT OPERATION TO PERFORM \n 1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION \n 5.POWER \n 6.FACTORIAL \n")
    a=int(input("ENTER SERIAL NUMBER OF YOUR OPERATION:"))
  


    if a==1:
        num1=int(input("ENTER FIRST VALUE:"))
        num2=int(input("ENTER SECOND VALUE:"))
        print(add(num1,num2))
    elif a==2:
        num1=int(input("ENTER FIRST VALUE:"))
        num2=int(input("ENTER SECOND VALUE:"))
        print(sub(num1,num2))
    elif a==3:
        num1=int(input("ENTER FIRST VALUE:"))
        num2=int(input("ENTER SECOND VALUE:"))
        print(multiply(num1,num2))
    elif a==4:
        num1=int(input("ENTER FIRST VALUE:"))
        num2=int(input("ENTER SECOND VALUE:"))
        print(divide(num1,num2))
    elif a==5:
        num1=int(input("ENTER BASE VALUE:"))
        num2=int(input("ENTER POWER:"))
        print(pow(num1,num2))
    elif a==6:
        num1=int(input("ENTER VALUE TO FIND FACTORIAL:"))
        print(fact(num1))


