#program to print pascals traingle using combinations

From math import factorial

n=int(input("ENTER NUMBER OF ROWS:"))  #input
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1): 
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")   #using n!/(r!(n-r)!)
    print()

