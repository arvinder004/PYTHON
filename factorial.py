# program to find factorial of any number

def fact(x):
    a=1
    for i in range(1,x+1):
        a*=i
    print(a)
n=int(input("enter a natural number to find factorial:"))
if n>0:
    fact(n)
elif n==0:
    print("1")
else:
    print("enter a valid value")
