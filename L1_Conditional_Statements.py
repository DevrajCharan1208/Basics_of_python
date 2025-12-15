n = int(input("Enter the day of the week (1 to 7) : "))
day = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

if (1 <= n <= 7):
    print (f"Name of the day {n} of the week is", day[n-1]+'day')
else:
    print ("Invalid Input")
    
    
    
   
n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

choices = '''
Choose operation to perform
 1.) Addition , +
 2.) Subtration , -
 3.) Division , /
 4.) Multiplication , x
    
    Enter integer digit as choice - 1,2,3,4 : '''    
    
choice = int(input(choices))

if (choice == 1):
    print (f"{n} + {m} = ", n+m)
elif (choice == 2):
    print (f"{n} - {m} = ", n-m)
elif (choice == 3):
    print (f"{n} / {m} = ", n/m)
elif (choice == 4):
    print (f"{n} x {m} = ", n*m)
else:
    print("Invalid Input")    
    
    
   
n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

if (n==m):
    print("Both are equal")    
elif (n > m):
    print(f"{m} is smaller")
else:
    print(f"{n} is smaller")



    
from math import pi
r = int(input("Enter radius for the circle: "))
area = pi*(r**2)
circum = 2*pi*r

if (r > 0 ):
    print (f"\nArea and circumference of the circle having radius {r} are: ")
    print(f" \nArea = {area:.2f} \nCircumference = {circum:.2f} ")
else:
    print("Invalid Input")




a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if (a>b):
    if (a>c):
        print (f" {a} is greater than both {b} and {c}")
    else:
        print (f"{a} is greater than {b} but not {c}")
else:
    if (a<c):
        print (f" {a} is lesser than both {b} and {c}")
    else:
        print (f" {a} is lesser than {b} but not {c}")




def Salary_A(sales):
    Basic = 4000
    HRA = Basic * 0.2
    DA = Basic * 1.1
    Conv = 500
    Incen = sales * 0.1
    Bon = 1000
    
    salary = Basic + HRA + DA + Conv + Incen + Bon
    return salary


def Salary_B(sales):
    Basic = 4000
    HRA = Basic * 0.1
    DA = Basic * 1.1
    Conv = 500
    Incen = sales * 0.04
    Bon = 500
    
    salary = Basic + HRA + DA + Conv + Incen + Bon
    return salary

sales = int(input("Enter sales: "))

if (sales < 0):
    print("Invalid Salary")
elif (sales >= 100000):
    print(f"Salary of the employee after {sales} is {Salary_A(sales):,}")
else:
    print(f"Salary of the employee after {sales} is {Salary_B(sales):,}")








phy = int(input("Enter marks for physics: "))
chy = int(input("Enter marks for chemistry: "))
mat = int(input("Enter marks for mathematics: "))
eng = int(input("Enter marks for english: "))
com = int(input("Enter marks for computer: "))

total = phy + chy + mat + eng + com
percentage = (total/500)*100

print (f"Student have scored total of {percentage:.2f} %")
print (' \n AND \n ')

if (percentage >= 90 ):
    print("Passed with Distinction")
elif (90 > percentage >= 80):
    print("Passed with First Class")
elif (80 > percentage >= 70):
    print("Passed with Second Class")
elif (70 > percentage >= 60):
    print("Passed with Third Class")
else: 
    print("Failed")
 

 
    
 
    
 
    
 
    
 
    
 
    
 
    
 