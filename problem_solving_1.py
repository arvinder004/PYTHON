#WAP to display a person's name, age and address in three different lines

print("""arvinder
19
66/70 laxmi colony hathital""")

#Write a program to swap 2 variables

a = 10
b = 20
print("VALUE OF a IS ",a,"\nVALUE OF b IS" , b)

a,b = b,a
print("VALUE OF a IS ",a,"\nVALUE OF b IS" , b)

#WAP to convert a float to integer

x = 6.9
print(x,type(x))
x = int(x)
print(x,type(x))

#WAP to take details from a student for ID CARD and then print it in different lines

name = input("ENTER YOUR NAME:")
age = int(input("ENTER YOUR AGE:"))
blood_group = input("ENTER YOUR BLOOD GROUP:")
dob = input("ENTER YOUR DATE OF BIRTH (DD/MM/YYYY):")

print(name)
print(age)
print(blood_group)
print(dob)


#WAP to take user input as integer then convert it to float

n = int(input("ENTER ANY INTEGER:"))
print(float(n))
