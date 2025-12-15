import math
print("Importing math ")
print ("Square root of 81 = ",math.sqrt(81))
print ("Factorial of 6 = ",math.factorial(6))
print("Value of sin(pi/2) = ",math.sin(math.pi/2))


import random
print("Importing random generating random integers and elements")
a = []
for i in range(5):
    a.append(random.randint(1,100))
print("Generating 5 random integers: ", a)

random_element = a[random.randint(0,4)]
print("Random element from the list: ", random_element)


import datetime

print("Importing and using datetime")
current = datetime.datetime.now()
print("Current Date and TIme: ", current)

today = datetime.date.today()
year = today.year
month = today.month
print (f"Current year: {year}, Current month: {month}")

import mainfile1
print("create a module named mainfile1 and using")
print("Square root of 81: ", mainfile1.square_rt(81))
print("Factorial of 6: ", mainfile1.fact(6))
print("Value of sin(pi/2): ", mainfile1.sine(mainfile1.pi_val/2))

print()
values = mainfile1.random_5()
print("5 random integers 1-100: ", values)

print("random element from list: ", mainfile1.random_element_list(values))


import mymath
print("create a module named mymath and using")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

addition = mymath.add(a, b)
difference = mymath.subtract(a, b)
product = mymath.multiply(a, b)
division = mymath.divide(a, b)

print("Addition: ", addition)
print("Subtraction: ", difference)
print("Multiplicatoin: ", product)
print("Division: ", division)




































